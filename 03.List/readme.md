# 📘 Python Lists – Complete Guide  

## 🔹 What is a List?  
A **list** in Python is a built-in data structure used to store **multiple items** in a single variable.  

- Lists are **ordered** (elements have an index starting from 0).  
- Lists are **mutable** (can be modified after creation).  
- Lists can store **different data types** (int, float, string, etc.).  
- Lists are defined using **square brackets `[ ]`**.  

```python
my_list = [10, 20, "Python", 3.14, True]
print(my_list)       # [10, 20, 'Python', 3.14, True]
print(type(my_list)) # <class 'list'>
```

## 🔹 List Operations

## 1. Creating a List
```
list1 = [1, 2, 3, 4, 5]      # integers
list2 = ["apple", "banana"]  # strings
list3 = [10, "hello", 3.5]   # mixed
empty_list = []              # empty
```

## 2. Accessing Elements
```
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry
```

## 3. Updating Elements
```
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']
```

## 4. Adding Elements
```
fruits = ["apple", "banana"]

# append() → add at end
fruits.append("cherry")

# insert(index, value) → add at position
fruits.insert(1, "mango")

# extend() → add multiple items
fruits.extend(["grapes", "orange"])

print(fruits)  
# ['apple', 'mango', 'banana', 'cherry', 'grapes', 'orange']
```

## 5. Removing Elements
```
fruits = ["apple", "banana", "cherry", "mango"]

fruits.remove("banana")  # remove by value
fruits.pop(1)            # remove by index
del fruits[0]            # delete element
fruits.clear()           # empty list
```

## 6. Searching & Checking
```
numbers = [10, 20, 30, 40]
print(20 in numbers)       # True
print(numbers.index(30))   # 2
print(numbers.count(10))   # 1
```
## 7. List Slicing
```
nums = [0, 1, 2, 3, 4, 5, 6]

print(nums[1:4])   # [1, 2, 3]
print(nums[:3])    # [0, 1, 2]
print(nums[4:])    # [4, 5, 6]
print(nums[::2])   # [0, 2, 4, 6]
print(nums[::-1])  # [6, 5, 4, 3, 2, 1, 0]
```
## 8. Sorting & Reversing
```
nums = [3, 1, 4, 2, 5]

nums.sort()              # ascending
nums.sort(reverse=True)  # descending
nums.reverse()           # reverse order
```
## 9. Copying a List
```
a = [1, 2, 3]
b = a.copy()
print(b)  # [1, 2, 3]
```
## 10. Joining Lists
```
list1 = [1, 2, 3]
list2 = [4, 5]

print(list1 + list2)  # concatenation
list1.extend(list2)   # extend method
```
## 11. Built-in Functions

```
numbers = [10, 20, 30, 40, 50]

print(len(numbers))   # 5
print(min(numbers))   # 10
print(max(numbers))   # 50
print(sum(numbers))   # 150
```

## 12. List Comprehension
```
squares = [x*x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

even = [x for x in range(10) if x % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]
```

## 📌 Summary – Common List Methods

```
Method	Description
append(x)	Add element at end
insert(i,x)	Insert at index i
extend(lst)	Add multiple elements
remove(x)	Remove first occurrence of x
pop(i)	Remove element at index i
clear()	Empty the list
index(x)	Get index of first occurrence of x
count(x)	Count occurrences of x
sort()	Sort list (ascending by default)
reverse()	Reverse order of list
copy()	Create a shallow copy
```