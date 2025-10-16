
# 🧠 Exception Handling in Python

## 📘 What is Exception Handling?

**Exception Handling** is a mechanism in Python to **handle runtime errors** — so your program doesn’t crash when something unexpected happens (like dividing by zero, missing files, or invalid input).

Instead of stopping the program, Python allows you to **catch** these errors and **handle them gracefully**.

---

## ⚙️ Basic Syntax

```python
try:
    # Code that may cause an error
    risky_code_here
except:
    # Code that runs if an error occurs
    handle_the_error
```

---

## 🔁 Full Syntax with All Blocks

```python
try:
    # Code that may raise an exception
    ...
except SomeError:
    # Handles that specific error
    ...
except AnotherError:
    # Handles another error type
    ...
else:
    # Executes only if NO exception occurs
    ...
finally:
    # Always executes (whether error occurs or not)
    ...
```

---

## 💡 Example

```python
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Invalid input. Please enter a number.")

else:
    print("Division successful.")

finally:
    print("Program execution completed.")
```

✅ **Output Example:**
```
Enter a number: 10
Enter another number: 0
You cannot divide by zero!
Program execution completed.
```

---

## 🧾 Common Types of Exceptions in Python

| Exception Name | Description |
|----------------|-------------|
| **Exception** | Base class for all exceptions |
| **ArithmeticError** | Base class for numeric calculation errors |
| **ZeroDivisionError** | Raised when dividing by zero |
| **ValueError** | Raised when a function gets the right type but wrong value |
| **TypeError** | Raised when operation is applied to wrong data type |
| **IndexError** | Raised when index is out of range in list/tuple |
| **KeyError** | Raised when key not found in dictionary |
| **NameError** | Raised when variable is not defined |
| **FileNotFoundError** | Raised when trying to open a file that doesn't exist |
| **IOError** | Raised when input/output operation fails |
| **ImportError** | Raised when import statement fails |
| **ModuleNotFoundError** | Raised when module is not found |
| **AttributeError** | Raised when invalid attribute reference is used |
| **MemoryError** | Raised when operation runs out of memory |
| **OverflowError** | Raised when calculation exceeds the limit for a numeric type |
| **RuntimeError** | Raised when an error does not fall under any category |
| **AssertionError** | Raised when an `assert` statement fails |
| **PermissionError** | Raised when trying to open or write a file without permission |
| **KeyboardInterrupt** | Raised when user interrupts program execution (Ctrl + C) |

---

## 🧰 Example — Handling Multiple Exceptions Together

```python
try:
    file = open("example.txt", "r")
    data = file.read()
    result = 10 / 0

except (FileNotFoundError, ZeroDivisionError) as e:
    print("Error occurred:", e)

finally:
    print("End of program")
```

---

## ✅ Best Practices

- Always handle **specific exceptions** (not just `except:` alone).
- Use `finally` to **close files or connections**.
- Use `with open()` to **automatically close files**.
- Log or print meaningful error messages.
