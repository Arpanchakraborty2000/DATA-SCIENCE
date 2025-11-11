# ⚙️ Python Generators — Complete Guide with Examples

A **generator** in Python is a special type of **iterator** that allows you to **iterate through data without storing it all in memory**.  
It yields values **one at a time**, only when requested — making it **memory efficient and fast**.

---

## 🧠 What is a Generator?

> A generator is a **function that contains one or more `yield` statements**.  
> Each time the function is called, it **pauses its state** and **returns a value** using `yield`, resuming from the same point next time.

---

## ✅ Example 1: Simple Generator

```python
def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # ❌ StopIteration
```
🧾 **Output:**
```
1
2
3
```

---

## 🔹 Example 2: Generator with For Loop

```python
def count_upto(n):
    for i in range(1, n + 1):
        yield i

for num in count_upto(5):
    print(num)
```
🧾 **Output:**
```
1
2
3
4
5
```

---

## 🔹 Example 3: Compare Generator vs List (Memory Usage)

Generators are **memory-efficient**, because they don’t store all elements at once.

```python
import sys

nums_list = [i for i in range(1000000)]
print("List size:", sys.getsizeof(nums_list))

nums_gen = (i for i in range(1000000))
print("Generator size:", sys.getsizeof(nums_gen))
```
🧾 **Output (approx):**
```
List size: 8697464 bytes
Generator size: 112 bytes
```

✅ Huge difference — Generators are much lighter.

---

## 🔹 Example 4: Infinite Generator

Generators can produce infinite data because they yield lazily.

```python
def infinite_numbers(start=1):
    while True:
        yield start
        start += 1

gen = infinite_numbers()
for num in gen:
    if num > 5:
        break
    print(num)
```
🧾 **Output:**
```
1
2
3
4
5
```

---

## 🔹 Example 5: Fibonacci Sequence Generator

```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(50):
    print(num, end=" ")
```
🧾 **Output:**
```
0 1 1 2 3 5 8 13 21 34
```

---

## 🔹 Example 6: Using `send()` with Generators (Advanced)

Generators can receive data using the `.send()` method.

```python
def greeter():
    name = yield "Enter your name:"
    yield f"Hello, {name}!"

gen = greeter()
print(next(gen))           # Start → "Enter your name:"
print(gen.send("Arpan"))   # Send → "Hello, Arpan!"
```
🧾 **Output:**
```
Enter your name:
Hello, Arpan!
```

---

## 🔹 Example 7: Generator Expression

Similar to list comprehensions but use **()`** instead of **[]**.

```python
gen = (x * x for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print(next(gen))  # 16
```
🧾 **Output:**
```
0
1
4
9
16
```

---

## 🔹 Example 8: Chaining Generators

You can connect generators together (pipeline).

```python
def numbers():
    for i in range(1, 6):
        yield i

def square(nums):
    for n in nums:
        yield n * n

for val in square(numbers()):
    print(val)
```
🧾 **Output:**
```
1
4
9
16
25
```

---

## 🧩 Generator vs Iterator

| Feature | Iterator | Generator |
|----------|-----------|-----------|
| Implementation | Class with `__iter__()` and `__next__()` | Function using `yield` |
| Memory | Uses more memory | Very memory efficient |
| Syntax | Verbose | Simple and readable |
| Return | Returns manually | Uses `yield` |
| Infinite Sequence | Harder | Easier |

---

## 💡 Advantages of Generators

✅ **Memory Efficient** — Processes one item at a time  
✅ **Lazy Evaluation** — Fetches data only when needed  
✅ **Readable Code** — Cleaner than custom iterator classes  
✅ **Useful for Large Data Streams** — Ideal for big files or data pipelines  

---

## ⚙️ Real-World Example: Reading Large Files

```python
def read_file_line_by_line(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

for line in read_file_line_by_line("data.txt"):
    print(line)
```
✅ Reads file **line-by-line** — no memory overload for large files.

---

## 🧱 Summary

| Concept | Description |
|----------|-------------|
| **Generator** | A function that yields values one at a time |
| **Keyword** | `yield` |
| **Type** | `<class 'generator'>` |
| **Memory Use** | Very low |
| **Can Be Infinite?** | ✅ Yes |
| **Example Use** | File reading, Fibonacci, data streaming |

---

### ✍️ Author
**Arpan Chakraborty**  
Python Generators — Simplified Explanation with Practical and Real-world Examples.
