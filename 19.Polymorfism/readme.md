# 🐍 Python Polymorphism Examples

This repository contains **examples of Polymorphism in Python**, demonstrating how the same operation or function can behave differently depending on the object or context.

---

## 🔹 What is Polymorphism?

**Polymorphism** in Python allows objects of different classes to be treated through a **common interface**.  
It comes in several forms:

- **Polymorphism with Functions/Methods**
- **Polymorphism with Abstract Classes**
- **Operator Overloading** (not covered here, but similar concept)

---

## 🔸 1. Polymorphism with Functions

### Example:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Polymorphic function
def print_area(shape):
    print(f"The area is {shape.area()}")  # Calls the correct method for each object

# Usage
rectangle = Rectangle(4, 3)
circle = Circle(10)

print_area(rectangle)  # Output: The area is 12
print_area(circle)     # Output: The area is 314.0
```

Explanation:
The same function print_area() works for both Rectangle and Circle, demonstrating polymorphism.

## 🔸 2. Polymorphism with Methods (Method Overriding)
Example:
```python
class Animal:
    def speak(self):
        print("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()


Output:

Dog barks
Cat meows
Some generic animal sound

```
Explanation:
Even though all objects are treated as Animal, the correct method is called based on the actual object type.

## 🔸 3. Polymorphism with Abstract Classes

Using abstract classes ensures that all subclasses implement required methods.

Example:
```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Polymorphic function
def print_area(shape: Shape):
    print(f"The area is {shape.area()}")

# Usage
rectangle = Rectangle(4, 3)
circle = Circle(10)

print_area(rectangle)  # Output: The area is 12
print_area(circle)     # Output: The area is 314.0

```

Explanation:

Shape is an abstract class and cannot be instantiated.

Both Rectangle and Circle must implement area().

print_area() works polymorphically on any subclass of Shape.

## 🔸 4. Summary Table
Type of Polymorphism	Description
Function/Method Polymorphism	Same function works on different object types
Method Overriding	Subclass provides a specific implementation of a parent method
Abstract Class Polymorphism	Base class defines interface; subclasses implement it

## ✅ Key Takeaways

Polymorphism allows flexible and reusable code.

Python does not require explicit types; it works based on duck typing.

Using abstract classes improves code reliability by enforcing required methods in subclasses.