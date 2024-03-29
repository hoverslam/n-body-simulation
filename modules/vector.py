from __future__ import annotations
import math


class Vector3:
    """This class represents vectors in a 3D vector space. 
    """
          
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        """Initialize class.

        Args:
            x (float): X-coordinate of this vector.
            y (float): Y-coordinate of this vector.
            z (float): Z-coordinate of this vector.
        """
        self.x, self.y, self.z = x, y, z 
         
    def __add__(self, v: Vector3) -> Vector3:
        """Returns the sum of this vector and v.

        Args:
            v (Vector3): A vector in 3D space.

        Returns:
            Vector3: A vector in 3D space.
        """
        return Vector3(self.x + v.x,
                       self.y + v.y,
                       self.z + v.z)
   
    def __sub__(self, v: Vector3) -> Vector3:
        """Returns the sum of this vector and -1 * v.

        Args:
            v (Vector3): A vector in 3D space.

        Returns:
            Vector3: A vector in 3D space.
        """
        return Vector3(self.x - v.x,
                       self.y - v.y,
                       self.z - v.z)
      
    def __getitem__(self, item: int) -> float:
        """Returns the coordinate specified by an index.

        Args:
            item (int): The index of the coordinate (x = 0, y = 1, z = 2)

        Raises:
            IndexError: Maximum index is 2 since this vector has only 3 coordinates.  

        Returns:
            float: One coordinate of this vector.
        """
        if item == 0: 
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("This vector has only 3 coordinates.")
        
    def __str__(self) -> str:
        """Returns a readable form of the vector coordinates.

        Returns:
            str: Coordinates of this vector.
        """
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)

    def times(self, f: float) -> Vector3:
        """Returns the product of this vector and f.

        Args:
            f (float): A number by which this vector is multiplied.

        Returns:
            Vector3: A vector in 3D space.
        """
        return Vector3(self.x * f,
                       self.y * f,
                       self.z * f)

    def length(self) -> float:
        """Returns the length (norm) of this vector.

        Returns:
            float: Length of this vector.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self) -> None:
        """Changes the length of this vector to 1. The direction and orientation is not affected.
        """
        length = self.length()
        self.x /= length
        self.y /= length
        self.z /= length
    
    def normalized(self) -> Vector3:
        """Returns a vector with the same direction and orientation, but length 1. 

        Returns:
            Vector3: A vector in 3D space.
        """
        length = self.length()
        
        return Vector3(self.x / length, 
                       self.y / length,
                       self.z / length)