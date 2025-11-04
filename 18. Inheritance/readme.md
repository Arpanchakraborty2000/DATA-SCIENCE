# 🐍 Python Inheritance — Complete Guide

This repository explains **Inheritance in Python (OOP)** with clear examples and code snippets.  
Inheritance allows one class to **acquire the properties and methods** of another class, promoting **reusability** and **cleaner code design**.

---

## 🔹 What is Inheritance?

Inheritance enables a new class (child/derived class) to **use the features of an existing class** (parent/base class).

### **Syntax:**
```python
class Parent:
    # parent class code

class Child(Parent):
    # child class code
```


## 🔸 1. Single Inheritance

When a child class inherits from one parent class.

Example:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

# Usage
dog1 = Dog("Buddy")
dog1.speak()


Output:

Buddy barks!
```
## 🔸 2. Multilevel Inheritance

When a class is derived from another derived class.

Example:

```python
class GrandParent:
    def feature1(self):
        print("Feature 1 from GrandParent")

class Parent(GrandParent):
    def feature2(self):
        print("Feature 2 from Parent")

class Child(Parent):
    def feature3(self):
        print("Feature 3 from Child")

# Usage
obj = Child()
obj.feature1()
obj.feature2()
obj.feature3()


Output:

Feature 1 from GrandParent
Feature 2 from Parent
Feature 3 from Child
```
## 🔸 3. Hierarchical Inheritance

When multiple child classes inherit from the same parent class.

Example:
```python
class Animal:
    def speak(self):
        print("Animals make sounds")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Usage
d = Dog()
c = Cat()
d.speak()
c.speak()


Output:

Dog barks
Cat meows
```
## 🔸 4. Multiple Inheritance

When a child class inherits from more than one parent class.

Example 1: (Basic Version)

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says woof! Owner: {self.owner}"

# Usage
dog1 = Dog("Buddy", "Arpan")
print(dog1.speak())


Output:

Buddy says woof! Owner: Arpan
```


Example 2: (Advanced Version — Using super() and **kwargs)
```python
class Animal:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

class Pet:
    def __init__(self, owner, **kwargs):
        super().__init__(**kwargs)
        self.owner = owner

class Dog(Animal, Pet):
    def __init__(self, name, owner):
        super().__init__(name=name, owner=owner)

    def speak(self):
        return f"{self.name} says woof! Owner: {self.owner}"

# Usage
dog = Dog("Tommy", "Arpan")
print(dog.speak())
```

✅ This version respects Method Resolution Order (MRO) and is more scalable.

## 🔸 5. Method Overriding

When a child class defines the same method as the parent, it overrides the parent’s version.

Example:
```python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started with a key")

# Usage
v = Vehicle()
c = Car()
v.start()
c.start()


Output:

Vehicle started
Car started with a key
```
## 🔸 6. Using super() in Inheritance

super() is used to call a method (usually the constructor) of the parent class.

Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.emp_id}")

# Usage
emp = Employee("Arpan", 28, "E101")
emp.show_info()


Output:

Name: Arpan, Age: 28, ID: E101
```
## 🧠 Summary Table
Type of Inheritance	Description	Example Classes
Single	One child inherits from one parent	Animal → Dog
Multilevel	Chain of inheritance	GrandParent → Parent → Child
Hierarchical	Multiple children inherit from same parent	Animal → Dog, Cat
Multiple	One child inherits from multiple parents	Dog(Animal, Pet)

### 🏁 Final Example: Combined Demonstration

```python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is ready to drive!")

class ElectricCar(Car):
    def start(self):
        super().start()
        print("Electric Car running silently ⚡")

# Usage
e_car = ElectricCar()
e_car.start()


Output:

Vehicle started
Car is ready to drive!
Electric Car running silently ⚡
```

## ✅ Key Takeaways

Inheritance promotes code reuse.

You can use super() to call parent methods.

Multiple inheritance requires careful use of MRO.

Method overriding allows customizing parent class behavior.