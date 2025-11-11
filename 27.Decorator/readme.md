# 🎨 Python Decorators — Complete Guide with Examples

A **decorator** in Python is a **function that modifies another function’s behavior** without changing its source code.  
Decorators are used extensively in frameworks like **Flask**, **Django**, and **FastAPI**.

---

## 🧠 What is a Decorator?

A decorator is a **higher-order function** that:
- Takes another function as an argument,
- Adds or alters its functionality,
- Returns a new function.

> Think of it as a **wrapper** that adds extra features before or after running the main function.

---

## ✅ Example 1: Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("✨ Before the function runs")
        func()
        print("✅ After the function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()
```
🧾 **Output:**
```
✨ Before the function runs
Hello, World!
✅ After the function runs
```

---

## ✅ Example 2: Decorator Without @ Syntax

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

def say_hello():
    print("Hi there!")

say_hello = my_decorator(say_hello)
say_hello()
```

---

## ✅ Example 3: Decorator with Arguments

```python
def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print("Function executed successfully!")
        return result
    return wrapper

@log_arguments
def add(a, b):
    return a + b

print("Result:", add(5, 10))
```
🧾 **Output:**
```
Arguments: (5, 10), {}
Function executed successfully!
Result: 15
```

---

## ✅ Example 4: Decorator That Returns a Value

```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_message():
    return "python decorators are powerful"

print(say_message())
```
🧾 **Output:**
```
PYTHON DECORATORS ARE POWERFUL
```

---

## ✅ Example 5: Using Multiple Decorators

```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Decorators in Python"

print(text())
```
🧾 **Output:**
```
<b><i>Decorators in Python</i></b>
```

---

## ✅ Example 6: Real-world Example — Logging Decorator

```python
import datetime

def log_time(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Running '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"[{datetime.datetime.now()}] Finished '{func.__name__}'!")
        return result
    return wrapper

@log_time
def process_data():
    print("Processing data...")

process_data()
```

---

## ✅ Example 7: Parameterized Decorator (Decorator Factory)

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello, Arpan!")

greet()
```
🧾 **Output:**
```
Hello, Arpan!
Hello, Arpan!
Hello, Arpan!
```

---

## ✅ Example 8: Class-based Decorator

```python
class DebugDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"🔍 Calling {self.func.__name__}")
        result = self.func(*args, **kwargs)
        print(f"✅ Finished {self.func.__name__}")
        return result

@DebugDecorator
def hello():
    print("Hello from class-based decorator!")

hello()
```

---

## 🧩 Common Use Cases of Decorators

| Use Case | Description |
|-----------|-------------|
| ✅ **Logging** | Log function calls or results |
| 🔐 **Authorization** | Restrict access based on user role |
| 🧪 **Performance Timing** | Measure execution time |
| ♻️ **Caching** | Store results of expensive operations |
| 🧰 **Validation** | Automatically check inputs |

---

## ⚙️ Real-world Example: Flask Route Decorator

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"
```

✅ Here, `@app.route('/')` connects the `home()` function to a URL endpoint.

---

## 🧱 Summary

| Concept | Description |
|----------|-------------|
| **Decorator** | A function that modifies another function’s behavior |
| **Syntax** | `@decorator_name` |
| **Return Value** | Usually returns a wrapper function |
| **Use Cases** | Logging, authorization, caching, etc. |
| **Advanced Type** | Class-based decorators |

---

### ✍️ Author
**Arpan Chakraborty**  
Python Decorators — Explained with Practical and Real-world Examples.
