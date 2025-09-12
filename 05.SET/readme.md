# 📘 Python Set

## 🔹 What is a Set?
- A **set** is an **unordered, mutable** collection of unique elements.  
- Duplicates are automatically removed.  
- Defined using `{}` or `set()` constructor.  

---

## 🔹 Creating Sets
```python
# Empty set
s1 = set()
print(s1)        # set()
print(type(s1))  # <class 'set'>

# Set with integers
s2 = {1, 2, 3, 4, 5}
print(s2)  # {1, 2, 3, 4, 5}

# Set with mixed data types
s3 = {1, "hello", 3.14, True}
print(s3)  # {1, 'hello', 3.14}  (True = 1, so unique)

# Duplicate values are removed
s4 = {1, 2, 2, 3, 4, 4}
print(s4)  # {1, 2, 3, 4}
```


## 🔹 Accessing Set Elements
```
Sets are unordered, so indexing is not allowed.
We use loops to access elements:

s = {10, 20, 30}
for i in s:
    print(i)
```
## 🔹 Adding Elements
```
s = {1, 2, 3}
s.add(4)          # add single element
print(s)          # {1, 2, 3, 4}

s.update([5, 6])  # add multiple elements
print(s)          # {1, 2, 3, 4, 5, 6}
```
## 🔹 Removing Elements
```
s = {1, 2, 3, 4}

s.remove(3)    # removes 3, error if not found
print(s)       # {1, 2, 4}

s.discard(10)  # no error if not found
print(s)       # {1, 2, 4}

x = s.pop()    # removes random element
print(x, s)

s.clear()      # removes all
print(s)       # set()
```

## 🔹 Set Operations (like in mathematics)
```
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print(a | b)             # {1, 2, 3, 4, 5, 6}
print(a.union(b))        # {1, 2, 3, 4, 5, 6}

# Intersection
print(a & b)             # {3, 4}
print(a.intersection(b)) # {3, 4}

# Difference
print(a - b)             # {1, 2}
print(a.difference(b))   # {1, 2}

# Symmetric Difference (elements not common)
print(a ^ b)                 # {1, 2, 5, 6}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}
```

## 🔹 Set Membership
```
s = {10, 20, 30}
print(10 in s)       # True
print(50 not in s)   # True
```
## 🔹 Other Useful Set Methods
```
s = {1, 2, 3}
t = {3, 4, 5}

print(s.issubset({1, 2, 3, 4}))   # True
print(s.issuperset({1, 2}))       # True
print(s.isdisjoint({5, 6}))       # True (no common elements)

# Copy
s2 = s.copy()
print(s2)   # {1, 2, 3}

🔹 Frozenset (Immutable Set)
fs = frozenset([1, 2, 3, 4])
print(fs)         # frozenset({1, 2, 3, 4})

# fs.add(5)  ❌ Error (frozenset is immutable)
```
# ✅ Summary of Set Functions
```
Function	Description
add()	Add single element
update()	Add multiple elements
remove()	Remove element (error if not found)
discard()	Remove element (no error if not found)
pop()	Remove and return random element
clear()	Remove all elements
union() / |	Returns union
intersection() / &	Returns intersection
difference() / -	Returns difference
symmetric_difference() / ^	Returns uncommon elements
issubset()	Check if set is subset
issuperset()	Check if set is superset
isdisjoint()	True if no elements in common
copy()	Copy set
frozenset()	Immutable set

```