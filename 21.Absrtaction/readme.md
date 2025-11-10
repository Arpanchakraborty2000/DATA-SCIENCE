# 🧩 Abstraction in Python

Abstraction is one of the core concepts of **Object-Oriented Programming (OOP)**.  
It focuses on **hiding complex implementation details** and **exposing only the necessary parts** of an object to the outside world.

---

## 🧠 **What is Abstraction?**

Abstraction allows us to define the **structure or behavior** of a system without revealing its implementation.  
In simple terms — it tells **what an object does**, not **how it does it**.

### 🔹 Real-life Example:
When you drive a car, you just use:
- The **steering wheel**
- The **brake pedal**
- The **accelerator**

You **don’t need to know** how the engine or fuel injection system works.  
That’s **abstraction**.

---

## ⚙️ **How to Implement Abstraction in Python**

Python provides abstraction through:
- **Abstract Base Classes (ABC)**
- **Abstract Methods**

We use the **`abc` module** (`from abc import ABC, abstractmethod`) to create abstract classes.

---

## ✅ **Example 1: Basic Abstraction using Abstract Class**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):  # Concrete subclass
    def start(self):
        print("🚗 Car engine started...")

    def stop(self):
        print("🚗 Car stopped safely.")

# Using the subclass
car = Car()
car.start()
car.stop()
```

### 🧾 **Output**
```
🚗 Car engine started...
🚗 Car stopped safely.
```

---

## ⚠️ **Trying to Instantiate Abstract Class**

```python
v = Vehicle()
```
❌ Output:
```
TypeError: Can't instantiate abstract class Vehicle with abstract methods start, stop
```

Abstract classes **cannot be instantiated directly** — they only act as **blueprints** for subclasses.

---

## ✅ **Example 2: Multiple Classes with Abstraction**

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Using abstraction
shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print(f"Area: {shape.area()} | Perimeter: {shape.perimeter()}")
```

### 🧾 **Output**
```
Area: 78.5 | Perimeter: 31.400000000000002
Area: 24 | Perimeter: 20
```

---

## ✅ **Example 3: Abstraction + Encapsulation Together**

```python
from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def balance(self):
        pass

class SavingsAccount(Bank):
    def __init__(self, account_no, balance):
        self.__account_no = account_no     # private variable
        self.__balance = balance           # private variable

    def balance(self):
        print(f"💰 Account {self.__account_no} balance is ₹{self.__balance}")

acc = SavingsAccount("1234XYZ", 50000)
acc.balance()
```

### 🧾 **Output**
```
💰 Account 1234XYZ balance is ₹50000
```

Here:
- **Abstraction:** `Bank` class hides how balance is calculated.
- **Encapsulation:** Account details (`__balance`, `__account_no`) are kept private.

---

## 🔍 **Key Takeaways**

| Concept | Description |
|----------|-------------|
| **Abstract Class** | A class that cannot be instantiated directly |
| **Abstract Method** | Declared but not implemented in the base class |
| **Module** | `abc` |
| **Purpose** | Enforce a consistent interface across subclasses |

---

## 🧩 **When to Use Abstraction**

- When multiple subclasses share a **common structure or interface**
- When you want to **hide implementation details**
- When designing **frameworks or APIs** where subclasses must implement specific methods

---

## 🧱 **Summary**

- ✅ Abstraction focuses on **what to do**, not **how to do it**.  
- 🧱 It improves **readability**, **security**, and **code structure**.  
- ⚙️ Use `@abstractmethod` to enforce subclass implementation.

---

### ✍️ **Author**
**Arpan Chakraborty**  
Abstraction Examples in Python — with Abstract Classes, Methods, and Real-world Implementations.
