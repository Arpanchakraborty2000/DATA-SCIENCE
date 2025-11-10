# 🪄 Magic Methods (Dunder Methods) in Python

Magic methods, also known as **dunder methods** (short for *double underscore*), are special built-in methods in Python that **start and end with double underscores**.  
They allow developers to **customize how objects behave** in common operations like printing, addition, comparison, iteration, etc.

---

## 🧠 **What Are Magic Methods?**

Magic methods are **automatically invoked** by Python for specific operations — you don't call them directly.  
They make your objects act like **built-in types**.

👉 Example:
```python
print(len([1, 2, 3]))
```
Internally calls:
```python
[1, 2, 3].__len__()
```

---

## 🧩 **Naming Convention**

All magic methods are written like this:
```
__methodname__()
```

### Common Examples:
- `__init__()` → Constructor
- `__str__()` → String representation
- `__add__()` → Used with `+` operator
- `__len__()` → Used with `len()`
- `__getitem__()` → Used for indexing
- `__call__()` → Makes object callable

---

## ✅ **1. `__init__()` – Constructor**
Called automatically when an object is created.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Arpan", 25)
print(p1.name)
```
🧾 **Output:**
```
Arpan
```

---

## ✅ **2. `__str__()` – String Representation**
Defines how the object is represented when printed.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

p1 = Person("Riya", 23)
print(p1)
```
🧾 **Output:**
```
Person(Name: Riya, Age: 23)
```

---

## ✅ **3. `__add__()` – Operator Overloading**
Lets you define custom behavior for the `+` operator.

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
🧾 **Output:**
```
(6, 8)
```

---

## ✅ **4. `__len__()` – Used with `len()`**
Defines custom behavior when `len(object)` is used.

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

b1 = Book("Python Mastery", 350)
print(len(b1))
```
🧾 **Output:**
```
350
```

---

## ✅ **5. `__eq__()` – Equality Comparison (`==`)**
Defines how two objects are compared using `==`.

```python
class Student:
    def __init__(self, roll):
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll

s1 = Student(101)
s2 = Student(101)
print(s1 == s2)
```
🧾 **Output:**
```
True
```

---

## ✅ **6. `__getitem__()` – Enables Indexing**
Allows objects to be accessed like lists.

```python
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

ml = MyList([10, 20, 30, 40])
print(ml[2])
```
🧾 **Output:**
```
30
```

---

## ✅ **7. `__call__()` – Callable Objects**
Makes an object behave like a function.

```python
class Greeter:
    def __call__(self, name):
        print(f"Hello, {name} 👋")

greet = Greeter()
greet("Arpan")
```
🧾 **Output:**
```
Hello, Arpan 👋
```

---

## 🧠 **Other Common Magic Methods**

| Method | Purpose |
|---------|----------|
| `__init__()` | Constructor (initialization) |
| `__del__()` | Destructor (cleanup before object deletion) |
| `__repr__()` | Developer-friendly string representation |
| `__str__()` | User-friendly string representation |
| `__add__()`, `__sub__()`, `__mul__()` | Operator overloading |
| `__eq__()`, `__lt__()`, `__gt__()` | Comparison operations |
| `__len__()` | Define object length |
| `__getitem__()` | Get item by index |
| `__setitem__()` | Set item by index |
| `__iter__()` | Make object iterable |
| `__next__()` | Return next item in iteration |
| `__call__()` | Make object callable |

---

## 🧱 **In Short**

| Feature | Description |
|----------|-------------|
| Magic Methods | Built-in methods with `__` prefix/suffix |
| Also Known As | Dunder Methods |
| Example | `__init__`, `__str__`, `__add__`, `__len__` |
| Purpose | Customize class behavior for built-in operations |

---

## 🧩 **Summary**

- 🪄 Magic methods make custom classes behave like built-in types.  
- ⚙️ Used for **operator overloading**, **string formatting**, **iteration**, and more.  
- 🧱 Always written with **double underscores** (e.g., `__init__`, `__str__`).

---

### ✍️ **Author**
**Arpan Chakraborty**  
Magic Methods in Python — Explained with Examples for OOP and Operator Overloading.
