# 🧩 Encapsulation in Python

Encapsulation is one of the fundamental principles of **Object-Oriented Programming (OOP)**.  
It means **binding data (variables)** and **methods (functions)** together into a single unit (class), and **restricting direct access** to some of the object's components.

---

## 🧠 **Why Encapsulation?**
- To protect data from being modified accidentally.  
- To maintain control over how variables are accessed or modified.  
- To hide implementation details and expose only necessary information.

---

## 🏗️ **Types of Encapsulation in Python**

| Access Modifier | Syntax | Description |
|-----------------|---------|--------------|
| Public | `self.name` | Accessible from anywhere |
| Protected | `self._name` | Accessible within the class and its subclasses |
| Private | `self.__name` | Accessible only inside the class |

---

## 📘 **1. Public Members Example**

```python
class Student:
    def __init__(self, name, age):
        self.name = name   # Public variable
        self.age = age     # Public variable

student1 = Student("Arpan", 22)

print(student1.name)  # ✅ Accessible
print(student1.age)   # ✅ Accessible
```

### 🧾 Output:
```
Arpan
22
```

---

## 🔒 **2. Protected Members Example**

Protected variables are defined using a **single underscore** (`_var`).  
They are *accessible but should not be modified directly* outside the class.

```python
class Person:
    def __init__(self, name, age):
        self._name = name   # Protected variable
        self._age = age     # Protected variable

class Employee(Person):
    def show_details(self):
        print(f"Name: {self._name}, Age: {self._age}")

emp = Employee("Riya", 25)
emp.show_details()

# Direct access (possible, but not recommended)
print(emp._name)
```

### 🧾 Output:
```
Name: Riya, Age: 25
Riya
```

---

## 🔐 **3. Private Members Example**

Private variables are defined using **double underscores** (`__var`).  
They are *name-mangled* to prevent accidental access from outside the class.

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private variable
        self.__balance = balance                # Private variable

    def show_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ₹{self.__balance}")

account = BankAccount("12345XYZ", 50000)
account.show_balance()

# ❌ Direct access (will cause error)
# print(account.__balance)

# ✅ Access through name mangling (not recommended)
print(account._BankAccount__balance)
```

### 🧾 Output:
```
Account Number: 12345XYZ
Balance: ₹50000
50000
```

---

## ⚙️ **4. Getter and Setter Methods (Manual Style)**

Encapsulation also means providing **controlled access** to private or protected variables using **getter** and **setter** methods.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter
    def get_name(self):
        return self._name

    # Setter
    def set_name(self, name):
        if len(name) > 1:
            self._name = name
        else:
            print("❌ Name must have at least 2 characters.")

person1 = Person("Arpan", 25)

print(person1.get_name())
person1.set_name("Riya")
print(person1.get_name())
```

### 🧾 Output:
```
Arpan
Riya
```

---

## 🧱 **5. Encapsulation using `@property` Decorator (Pythonic Way)**

Python provides a cleaner way to define getters and setters using `@property`.

```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value
        else:
            print("❌ Salary must be positive.")

emp = Employee("Arpan", 40000)
print(emp.salary)     # Calls getter

emp.salary = 50000    # Calls setter
print(emp.salary)
```

### 🧾 Output:
```
40000
50000
```

---

## 🔄 **Comparison Table**

| Type | Syntax | Access Outside Class | Recommended Use |
|------|---------|----------------------|-----------------|
| Public | `self.name` | ✅ Yes | When data is safe to expose |
| Protected | `self._name` | ⚠️ Yes (by convention protected) | Use in inheritance |
| Private | `self.__name` | ❌ No (uses name mangling) | When data must be hidden |

---

## 🧩 **Summary**

- ✅ **Encapsulation** helps in **data protection** and **controlled access**.  
- ⚙️ Use **getters/setters** to safely access or modify data.  
- 🧱 Prefer **@property** decorators for clean and Pythonic code.

---

### ✍️ **Author**
**Arpan Chakraborty**  
Encapsulation Examples in Python — with Public, Protected, Private, Getter & Setter Implementations.
