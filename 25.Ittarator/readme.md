# 🔁 Python Iterators — Complete Guide with Examples

An **iterator** in Python is an object that allows you to **traverse through elements one at a time**, without storing all of them in memory.  
It’s a **memory-efficient** way of looping through data.

---

## 🧠 **What is an Iterator?**

An **iterator** is an object that implements two methods:

| Method | Description |
|---------|-------------|
| `__iter__()` | Returns the iterator object itself |
| `__next__()` | Returns the next element from the sequence |

When there are **no more items**, `StopIteration` is raised.

---

## ✅ **Example 1: Simple Iterator**

```python
nums = [1, 2, 3, 4]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
# print(next(it))  # ❌ StopIteration
```

---

## 🔹 **Example 2: Using for loop (Python’s internal iterator)**

```python
nums = [10, 20, 30]

for n in nums:
    print(n)
```

Internally, Python does this:
```python
it = iter(nums)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
```

---

## 🔹 **Example 3: Creating a Custom Iterator Class**

```python
class CountUpto:
    def __init__(self, limit):
        self.limit = limit
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.limit:
            val = self.count
            self.count += 1
            return val
        else:
            raise StopIteration

numbers = CountUpto(5)
for num in numbers:
    print(num)
```

---

## 🔹 **Example 4: Infinite Iterator (⚠️ Use Carefully)**

```python
class InfiniteCounter:
    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num

counter = InfiniteCounter(10)
for c in counter:
    print(c)
    if c > 15:
        break
```

---

## 🔹 **Example 5: Iterator vs Iterable**

| Term | Meaning | Example |
|------|----------|----------|
| **Iterable** | Has `__iter__()` but no `__next__()` | list, tuple, string |
| **Iterator** | Has both `__iter__()` and `__next__()` | Object from `iter()` |

```python
nums = [1, 2, 3]
print(hasattr(nums, '__iter__'))   # ✅ True
print(hasattr(nums, '__next__'))   # ❌ False

it = iter(nums)
print(hasattr(it, '__iter__'))     # ✅ True
print(hasattr(it, '__next__'))     # ✅ True
```

---

## 🔹 **Example 6: Using Iterators in File Handling**

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

✅ Advantage → Reads one line at a time (memory efficient).

---

## 🔹 **Example 7: Custom Iterator with Step Size**

```python
class StepIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration

for val in StepIterator(0, 10, 2):
    print(val)
```

---

## 🔹 **Example 8: Iterator with Custom Reset Method**

```python
class ResetIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        else:
            raise StopIteration

    def reset(self):
        self.count = 0

it = ResetIterator(3)
for i in it:
    print(i)

it.reset()
for i in it:
    print(i)
```

---

## 🔹 **Iterator vs Generator**

| Feature | Iterator | Generator |
|----------|-----------|-----------|
| Implementation | Class-based | Function with `yield` |
| Syntax | Uses `__iter__()` and `__next__()` | Uses `yield` keyword |
| Memory | Moderate | Very low (lazy) |

```python
def count_upto(n):
    for i in range(1, n+1):
        yield i

for num in count_upto(5):
    print(num)
```

---

## 💡 **Benefits of Iterators**

✅ Memory Efficient  
✅ Lazy Evaluation (fetch only when needed)  
✅ Customizable Iteration Logic  
✅ Foundation for Generators, Streams & Async IO  

---

## 🧱 **Summary Table**

| Concept | Description |
|----------|-------------|
| **Iterator** | Object that returns data one element at a time |
| **Methods** | `__iter__()` and `__next__()` |
| **StopIteration** | Raised when iteration ends |
| **Use Cases** | Loops, Files, Generators, Streams |

---

### ✍️ Author
**Arpan Chakraborty**  
Python Iterators — Explained with Simple, Custom, Infinite, and File-based Examples.
