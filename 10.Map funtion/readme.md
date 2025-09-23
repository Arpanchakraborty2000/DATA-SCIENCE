# 📘 map() Function in Python

## 🔹 What is `map()`?
The `map()` function applies a given function to all items in an iterable (like list, tuple, set, etc.).

It returns a **map object** (iterator), which can be converted to `list`, `tuple`, or `set`.

---

## 🔹 Syntax
```python
map(function, iterable, ...)
```

## ✅ Example 1: Square each number in a list
```
# Function to square
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)

print(result)          # map object
print(list(result))    # [1, 4, 9, 16, 25]
```
## ✅ Example 2: Using lambda with map
```
numbers = [1, 2, 3, 4, 5]

# Using lambda
result = map(lambda x: x**2, numbers)

print(list(result))  # [1, 4, 9, 16, 25]
```
## ✅ Example 3: Convert list of strings to integers
```
strings = ["10", "20", "30", "40"]

result = map(int, strings)

print(list(result))  # [10, 20, 30, 40]
```
## ✅ Example 4: Multiple Iterables with map()
```
If more than one iterable is passed, map() applies the function by taking one element from each iterable.

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)

print(list(result))  # [5, 7, 9]
```
## ✅ Example 5: Convert Celsius to Fahrenheit
```
celsius = [0, 10, 20, 30, 40]

result = map(lambda c: (c * 9/5) + 32, celsius)

print(list(result))  # [32.0, 50.0, 68.0, 86.0, 104.0]
```
## ✅ Example 6: Map with str.upper
```
words = ["hello", "world", "python"]

result = map(str.upper, words)

print(list(result))  # ['HELLO', 'WORLD', 'PYTHON']
```
##  Key Points / Operations with map()

Works with any iterable (list, tuple, set, dict, etc.).

Returns a map object (iterator) → must convert to list(), tuple(), or set() to view.

Can use user-defined functions or lambda expressions.

Supports multiple iterables.