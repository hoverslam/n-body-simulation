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
        self.force = Vector3()
        
    def move(self) -> None:
        """Move this body to a new position, according to the total force vector exerted on it, 
        and updates the current velocity accordingly.
        """
        self.velocity = self.velocity + self.force.times(1 / self.mass)
        self.position = self.position + self.velocity
    
    def distance_to(self, b: Body) -> float:
        """Return the distance from this body to the specified body.

        Args:
            b (Body): A celestial object.

        Returns:
            float: Distance to specified body.
        """
        return (self.position - b.position).length()
    
    def gravitational_force(self, b: Body) -> Vector3:
        """Return a vector representing the gravitational force exerted on this body by another.

        Args:
            b (Body): A celestial object.

        Returns:
            Vector3: Gravitational force as a vector.
        """
        G = 6.6743e-11
        direction = b.position - self.position
        distance = direction.length()
        force = G * ((self.mass * b.mass) / (distance * distance))
        
        return direction.normalized().times(force)
    
    def add_force(self, b: Body) -> None:
        """Add the gravitational force of the specified body to the cumulative force exerted on this.

        Args:
            b (Body): A celestial object.
        """
        self.force += self.gravitational_force(b)
    
    def reset_force(self) -> None:
        """Set the cumulative force exerted on this body to zero.
        """
        self.force = Vector3()