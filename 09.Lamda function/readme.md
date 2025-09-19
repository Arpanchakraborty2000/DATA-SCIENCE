# 🐍 Lambda Function in Python

A **lambda function** in Python is a small, anonymous (nameless) function defined using the keyword `lambda`.  
It is often used for short, simple operations where defining a full function with `def` would be overkill.

---

## 📌 Syntax
```python
lambda arguments: expression

lambda → keyword to define the function

arguments → inputs (can be 0 or more)

expression → a single expression whose result is returned automatically
```

## 📘 Example 1: Simple addition
```
add = lambda x, y: x + y
print(add(5, 3))   # Output: 8


This is the same as:

def add(x, y):
    return x + y

```

## 📘 Example 2: Square of a number
```
square = lambda n: n * n
print(square(4))   # Output: 16
```
## 📘 Example 3: Using with map(), filter(), sorted()
```
Double each number in a list
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)   # [2, 4, 6, 8, 10]

Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)     # [2, 4]

Sort by last letter
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda w: w[-1])
print(sorted_words)  # ['banana', 'apple', 'cherry']
```
## ✅ Key Points
```
Lambda functions are anonymous (no name unless assigned).

Used for short, one-line functions.

They can take any number of arguments, but only one expression.

Commonly used with functional programming tools like map, filter, and reduce.
```