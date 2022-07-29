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
            mass (float): The mass of this body in kilograms.
            radius (float): The radius of this body in meters.
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
        raise NotImplementedError
    
    def distance_to(self, b: Body) -> float:
        raise NotImplementedError
    
    def gravitational_force(self, b: Body) -> Vector3:
        raise NotImplementedError
    
    def add_force(self, b: Body) -> None:
        raise NotImplementedError
    
    def reset_force(self, b: Body) -> None:
        raise NotImplementedError