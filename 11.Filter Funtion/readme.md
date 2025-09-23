# 📘 filter() Function in Python

## 🔹 What is `filter()`?
The `filter()` function is used to **filter elements** from an iterable (list, tuple, set, etc.) based on a condition (`True`/`False`).

It applies a function to each element and keeps only those that return `True`.

It returns a **filter object (iterator)**, which can be converted to `list`, `tuple`, or `set`.

---

## 🔹 Syntax
```python
filter(function, iterable)
```

function → A function that returns True or False.

iterable → The sequence to filter (list, tuple, set, etc.).

## ✅ Example 1: Filter even numbers
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return n % 2 == 0

result = filter(is_even, numbers)

print(result)          # filter object
print(list(result))    # [2, 4, 6, 8, 10]
```
## ✅ Example 2: Using lambda with filter
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x > 5, numbers)

print(list(result))  # [6, 7, 8, 9, 10]
```
## ✅ Example 3: Filter strings starting with "P"
```
words = ["Python", "Java", "PHP", "C++", "Perl"]

result = filter(lambda w: w.startswith("P"), words)

print(list(result))  # ['Python', 'PHP', 'Perl']
```
## ✅ Example 4: Remove empty strings
```
data = ["hello", "", "world", "", "python"]

result = filter(None, data)

print(list(result))  # ['hello', 'world', 'python']
```
## 🔹 Key Points

Works with any iterable.

Returns a filter object (iterator) → convert using list(), tuple(), set().

The function should return True/False.

If None is passed as function, it removes falsy values (0, False, '', None).