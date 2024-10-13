# polymorphism_demo.py

import math

class Shape:
    """Base class for shapes."""
    
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("This method should be overridden by subclasses.")


class Rectangle(Shape):
    """Class to represent a rectangle."""
    
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Class to represent a circle."""
    
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
