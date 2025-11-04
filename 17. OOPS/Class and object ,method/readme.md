# Python OOP Basics: Class, Constructor, Object, and Methods

This repository contains examples and explanations of **Object-Oriented Programming (OOP)** concepts in Python, including classes, constructors, objects, and methods.

---

## **1. Class**

A **class** is a blueprint for creating objects. It defines **attributes** (data) and **methods** (functions) that the object will have.

### **Example:**

```python
class Car:
    color = "Red"  # Attribute

    def drive(self):  # Method
        print("The car is driving.")
```

## 2. Constructor (__init__)

A constructor is a special method that is called automatically when a new object is created. It initializes the object’s attributes.

### Example:

```python
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f"The {self.color} {self.brand} car is driving.")

# Creating objects
car1 = Car("Blue", "Honda")
car2 = Car("Black", "Toyota")

car1.drive()
car2.drive()


Output:

The Blue Honda car is driving.
The Black Toyota car is driving.

```

## 3. Object

An object is an instance of a class. Each object can have its own attributes and behavior.

```python
Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.name, p1.age)
print(p2.name, p2.age)
```

## 4. Methods

A method is a function defined inside a class. There are several types of methods:

### 4.1 Instance Methods

Operate on instances of the class. Most common type.
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

# Example
acc1 = BankAccount("Arpan", 5000)
acc1.deposit(500)
acc1.withdraw(300)
```
### 4.2 Class Methods

Operate on the class itself, not instances. Use @classmethod.
```python
class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Update raise amount
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)
```

### 4.3 Static Methods

Do not access class or instance attributes, used for utility functions. Use @staticmethod.
```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(10, 5))
```
## 5. Summary
Concept	Description
Class	Blueprint for objects
Object	Instance of a class
Constructor	Special method to initialize objects (__init__)
Instance Method	Method that operates on an object instance
Class Method	Method that operates on the class itself (@classmethod)
Static Method	Method that does not depend on class or instance (@staticmethod)
```python
6. Example Project: Bank Account

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

# Usage
acc1 = BankAccount("Arpan", 5000)
acc1.deposit(500)
acc1.withdraw(300)
print("Current balance:", acc1.get_balance())

```