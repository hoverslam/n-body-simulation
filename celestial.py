from __future__ import annotations
from vector import Vector3


class Body:
    """This class represents celestial bodies like stars, planets, asteroids, etc.
    """
    
    def __init__(self, position: Vector3, velocity: Vector3, mass: float, radius: float,
                 name: str = "", color: str = "lightgray") -> None:
        """Initialize class.

        Args:
            position (Vector3): The position from the origin.
            velocity (Vector3): The velocity of this body.
            mass (float): The mass of this body in kilogram.
            radius (float): The radius of this body in meter.
            name (str, optional): The name of this body. Defaults to "".
            color (str, optional): The color in which the body is displayed on the canvas. Defaults to "lightgray".
        """
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius
        self.name = name
        self.color = color
        
    def move(self, force: Vector3, dt: int) -> None:
        """Update the velocity of this body according to the given force vector, and 
        move it to the position.

        Args:
            force (Vector3): A force vector. 
            dt (int): Timestep size for the leap-frog scheme.
        """
        acceleration = force.times(1 / self.mass)
        self.velocity += acceleration.times(dt)
        self.position += self.velocity.times(dt)
    
    def distance_to(self, b: Body) -> float:
        """Return the distance from this body to the specified body.

        Args:
            b (Body): A celestial object.

        Returns:
            float: Distance to specified body.
        """
        return (self.position - b.position).length()
    
    def gravitational_force(self, b: Body, eps: float = 1e4) -> Vector3:
        """Return a vector representing the gravitational force exerted on this body by another.

        Args:
            b (Body): A celestial object.
            eps (float): Softening parameter to prevent numerical divergences.

        Returns:
            Vector3: Gravitational force as a vector.
        """
        G = 6.6743e-11
        direction = b.position - self.position
        distance = direction.length()
        force = (G * self.mass * b.mass) / (distance * distance + eps * eps)
        
        return direction.normalized().times(force)