# 📘 Tuples in Python

## 🔹 What is a Tuple?
- A tuple is an **ordered, immutable (unchangeable)** collection of elements.  
- Tuples can store **different data types**.  
- Defined using `()` parentheses.  

---

## 🔹 Creating Tuples
```python
# Empty tuple
t1 = ()

# Tuple with integers
t2 = (1, 2, 3, 4, 5)

# Tuple with mixed data types
t3 = (1, "hello", 3.14, True)

# Nested tuple
t4 = (1, (2, 3), (4, 5))

# Tuple without parentheses (packing)
t5 = 10, 20, 30

# Single-element tuple (comma required)
t6 = (10,)
```

## 🔹 Tuple Operations
```
t = (1, 2, 3, 4, 5)

# Indexing
print(t[0])   # 1
print(t[-1])  # 5

# Slicing
print(t[1:4])  # (2, 3, 4)

# Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)

# Repetition
print(t1 * 3)  # (1, 2, 1, 2, 1, 2)

# Membership test
print(3 in t)      # True
print(6 not in t)  # True
```

## 🔹 Tuple Functions
```
nums = (10, 20, 30, 40, 10)

print(len(nums))       # 5
print(max(nums))       # 40
print(min(nums))       # 10
print(sum(nums))       # 110
print(sorted(nums))    # [10, 10, 20, 30, 40]
print(tuple(sorted(nums, reverse=True)))  # (40, 30, 20, 10, 10)
```

## 🔹 Tuple Methods
```
nums = (10, 20, 30, 10, 40, 10)

print(nums.count(10))   # 3 (how many times 10 occurs)
print(nums.index(30))   # 2 (first occurrence of 30)
```
## 🔹 Tuple Unpacking
```
# Simple unpacking
t = (100, 200, 300)
a, b, c = t
print(a, b, c)  # 100 200 300

# Extended unpacking
t2 = (1, 2, 3, 4, 5)
a, *b, c = t2
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```
## 🔹 Nested Tuples
```
t = (1, (2, 3), (4, (5, 6)))

print(t[1])       # (2, 3)
print(t[2][1][0]) # 5
```
## 🔹 Iterating Over Tuple
```
t = ("apple", "banana", "cherry")
for item in t:
    print(item)
```
## 🔹 Tuple Packing and Unpacking
```
# Packing
pack_tup = 10, 20, 30
print(pack_tup)  # (10, 20, 30)

# Unpacking
a, b, c = pack_tup
print(a, b, c)  # 10 20 30
```
## 🔹 Tuple as Dictionary Keys
```
Tuples are hashable, unlike lists, so they can be used as keys in dictionaries.

locations = {
    (28.61, 77.20): "Delhi",
    (19.07, 72.87): "Mumbai"
}
print(locations[(28.61, 77.20)])  # Delhi
```
# ✅ Key Points

* Tuples are immutable (you can’t change elements).

* Faster than lists for iteration.

* Used as keys in dictionaries and for fixed data sets.