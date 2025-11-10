# ⚙️ Operator Overloading in Python

Operator Overloading is a concept in **Object-Oriented Programming (OOP)** that allows you to **customize how operators behave** when applied to user-defined objects.

---

## 🧠 What is Operator Overloading?

Normally, operators like `+`, `-`, `*`, and `==` work with Python’s built-in types.  
But with operator overloading, you can **define how these operators behave** for your own classes.

### Example:
```python
a = 10
b = 20
print(a + b)   # 30
```
Here, `+` adds two integers.  
With operator overloading, we can redefine `+` to work for custom objects.

---

## ❌ Without Operator Overloading

If you try to use `+` between objects of a custom class, Python throws an error.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1 + p2)   # ❌ Error
```
🧾 Output:
```
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

---

## ✅ With Operator Overloading

We can redefine the `+` operator using the **magic method** `__add__()`.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1 + p2)
```
🧾 Output:
```
(6, 8)
```

---

## 🔹 Common Magic Methods for Operator Overloading

| Operator | Magic Method | Example |
|-----------|---------------|----------|
| `+` | `__add__(self, other)` | `a + b` |
| `-` | `__sub__(self, other)` | `a - b` |
| `*` | `__mul__(self, other)` | `a * b` |
| `/` | `__truediv__(self, other)` | `a / b` |
| `//` | `__floordiv__(self, other)` | `a // b` |
| `%` | `__mod__(self, other)` | `a % b` |
| `**` | `__pow__(self, other)` | `a ** b` |
| `==` | `__eq__(self, other)` | `a == b` |
| `<` | `__lt__(self, other)` | `a < b` |
| `>` | `__gt__(self, other)` | `a > b` |

---

## 🔹 Example: Overloading `-` and `*` Operators

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

n1 = Number(10)
n2 = Number(3)

print("Subtraction:", n1 - n2)
print("Multiplication:", n1 * n2)
```
🧾 Output:
```
Subtraction: 7
Multiplication: 30
```

---

## 🔹 Example: Overloading `==` Operator

```python
class Student:
    def __init__(self, roll):
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll

s1 = Student(101)
s2 = Student(101)
s3 = Student(102)

print(s1 == s2)  # True
print(s1 == s3)  # False
```
🧾 Output:
```
True
False
```

---

## 🔹 Example: Real-world Vector Overloading

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(1, 3)

print(v1 + v2)
print(v1 * 3)
```
🧾 Output:
```
Vector(3, 7)
Vector(6, 12)
```

---

## 🧠 Why Use Operator Overloading?

✅ Makes objects behave like **built-in types**  
✅ Improves **code readability and expressiveness**  
✅ Useful in **mathematical modeling, games, and data structures**  

---

## 🧱 Key Concepts

| Concept | Description |
|----------|-------------|
| **Operator Overloading** | Redefining behavior of operators for custom classes |
| **Implemented Using** | Magic methods like `__add__`, `__eq__`, etc. |
| **Advantage** | Makes objects intuitive and easy to use |
| **Example** | `a + b` → `a.__add__(b)` |

---

## 🧩 Summary

- ⚙️ Operator overloading allows you to **customize operators** for your own classes.  
- 🧱 Achieved using **special methods** like `__add__`, `__sub__`, `__eq__`, etc.  
- 💡 Helps make objects behave like **built-in Python types**.  

---

### ✍️ Author  
**Arpan Chakraborty**  
Operator Overloading in Python — Explained with Magic Methods and Real-world Examples.
