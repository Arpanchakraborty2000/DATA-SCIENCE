# 📘 Python Dictionary

## 🔹 What is a Dictionary?
A **Dictionary** in Python is an **unordered, mutable, and key-value pair collection**.

- Keys are **unique** and **immutable** (string, number, tuple).
- Values can be of **any data type** (list, dict, int, etc.).
- Defined using `{}` braces or `dict()` constructor.

---

## 🔹 Creating a Dictionary
```python
# Empty dictionary
d1 = {}
print(d1)   # {}

# Using dict() constructor
d2 = dict(name="Arpan", age=24)
print(d2)   # {'name': 'Arpan', 'age': 24}

# Dictionary with mixed keys
student = {"name": "Arpan", "age": 24, "marks": [90, 85, 92]}
print(student)  # {'name': 'Arpan', 'age': 24, 'marks': [90, 85, 92]}
```

## 🔹 Accessing Dictionary Elements
```
student = {"name": "Arpan", "age": 24, "marks": 90}

# Access using key
print(student["name"])   # Arpan

# Access using get()
print(student.get("age"))   # 24
print(student.get("grade", "Not Found"))  # Not Found (default value)
```
## 🔹 Adding / Updating Elements
```
student["grade"] = "A"   # Add new key-value pair
student["marks"] = 95    # Update value
print(student)  
# {'name': 'Arpan', 'age': 24, 'marks': 95, 'grade': 'A'}
```
## 🔹 Removing Elements
```
# pop() – removes a specific key
student.pop("age")
print(student)  # {'name': 'Arpan', 'marks': 95, 'grade': 'A'}

# popitem() – removes last inserted key-value pair
student.popitem()
print(student)  # {'name': 'Arpan', 'marks': 95}

# del – delete key or whole dictionary
del student["marks"]
print(student)  # {'name': 'Arpan'}

# clear() – remove all items
student.clear()
print(student)  # {}
```
## 🔹 Dictionary Methods & Operations
```
student = {"name": "Arpan", "age": 24, "marks": 90}

# keys() – returns all keys
print(student.keys())  # dict_keys(['name', 'age', 'marks'])

# values() – returns all values
print(student.values())  # dict_values(['Arpan', 24, 90])

# items() – returns key-value pairs
print(student.items())  # dict_items([('name', 'Arpan'), ('age', 24), ('marks', 90)])

# copy() – shallow copy
student_copy = student.copy()
print(student_copy)

# update() – merge dictionaries
extra = {"grade": "A", "city": "Kolkata"}
student.update(extra)
print(student)
# {'name': 'Arpan', 'age': 24, 'marks': 90, 'grade': 'A', 'city': 'Kolkata'}
```
## 🔹 Dictionary Traversal (Looping)
```
student = {"name": "Arpan", "age": 24, "marks": 90}

# Loop through keys
for k in student:
    print(k, ":", student[k])

# Loop using items()
for k, v in student.items():
    print(k, "->", v)
```
## 🔹 Dictionary Comprehension
```
# Square numbers dictionary
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtered dictionary
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```
## 🔹 Nested Dictionary
```
students = {
    "s1": {"name": "Arpan", "marks": 90},
    "s2": {"name": "Riya", "marks": 85}
}

print(students["s1"]["name"])  # Arpan
print(students["s2"]["marks"]) # 85
```
# ✅ Summary of Operations

### Create → {} or dict()

### Access → [], get()

### Add/Update → dict[key] = value

### Remove → pop(), popitem(), del, clear()

### Methods → keys(), values(), items(), update(), copy()

### Loop → for k, v in dict.items()

### Advanced → Comprehension, Nested Dict