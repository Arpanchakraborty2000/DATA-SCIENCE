# ⚠️ Custom Exceptions in Python

Custom Exceptions are **user-defined error classes** that allow you to handle **specific error cases** in a more descriptive and readable way.

They make your programs more robust, clean, and easy to debug.

---

## 🧠 What is a Custom Exception?

Python already provides many built-in exceptions like `ValueError`, `TypeError`, `ZeroDivisionError`, etc.  
But in large applications, you might want to raise **your own exceptions** to handle domain-specific errors.

👉 For example:
- `InvalidAgeError`
- `InsufficientFundsError`
- `InvalidAccountError`

These make your code more meaningful and professional.

---

## ✅ Basic Example: Custom Exception

```python
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above to register.")
    else:
        print("✅ Age is valid for registration.")

try:
    check_age(15)
except InvalidAgeError as e:
    print("Error:", e)
```
🧾 **Output:**
```
Error: Age must be 18 or above to register.
```

---

## 🧩 Example: Custom Exception with `__init__()` and `__str__()`

You can customize the error message by defining `__init__()` and `__str__()` methods.

```python
class BalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"❌ Insufficient balance: Tried to withdraw ₹{self.amount}, but only ₹{self.balance} available."

def withdraw(balance, amount):
    if amount > balance:
        raise BalanceError(balance, amount)
    else:
        print(f"✅ Withdraw successful! Remaining balance: ₹{balance - amount}")

try:
    withdraw(1000, 2000)
except BalanceError as e:
    print(e)
```
🧾 **Output:**
```
❌ Insufficient balance: Tried to withdraw ₹2000, but only ₹1000 available.
```

---

## 🔹 Multiple Custom Exceptions

You can define and handle multiple custom exceptions in one program.

```python
class InvalidAccountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

def transfer(amount, balance, account):
    if account != "12345":
        raise InvalidAccountError("Account number not found!")
    elif amount > balance:
        raise InsufficientFundsError("Insufficient balance for this transfer.")
    else:
        print("✅ Transfer successful!")

try:
    transfer(5000, 3000, "67890")
except InvalidAccountError as e:
    print("Account Error:", e)
except InsufficientFundsError as e:
    print("Balance Error:", e)
```
🧾 **Output:**
```
Account Error: Account number not found!
```

---

## 🔹 Custom + Built-in Exceptions

You can mix custom exceptions with built-in ones.

```python
class NegativeNumberError(Exception):
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot find square root of negative number.")
    import math
    return math.sqrt(num)

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Custom Exception:", e)
except ValueError as e:
    print("Built-in Exception:", e)
```
🧾 **Output:**
```
Custom Exception: Cannot find square root of negative number.
```

---

## 🧱 **Key Concepts**

| Concept | Description |
|----------|-------------|
| **Custom Exception** | User-defined error class extending `Exception` |
| **Raise** | Use `raise CustomError("message")` |
| **Catch** | Use `try ... except CustomError:` |
| **Custom Message** | Override `__init__()` and `__str__()` for better output |

---

## 💡 **Best Practices**

✅ Always inherit from `Exception` (not `BaseException`)  
✅ Use **meaningful names** (e.g., `FileNotFoundError`, `UserAuthError`)  
✅ Keep exception classes simple and clean  
✅ Use logging to record exceptions in production  

---

## 🧩 Example Summary

```python
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise CustomError("This is a custom exception example!")
except CustomError as e:
    print("Caught:", e)
```
🧾 **Output:**
```
Caught: This is a custom exception example!
```

---

## 🧠 Why Use Custom Exceptions?

✅ Provides clear and descriptive error messages  
✅ Helps handle business-specific logic (e.g., banking, login systems)  
✅ Improves debugging and maintainability  

---

### ✍️ **Author**
**Arpan Chakraborty**  
Custom Exceptions in Python — Explained with Practical and Real-world Examples.
