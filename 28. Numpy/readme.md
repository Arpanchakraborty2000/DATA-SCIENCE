# ⚙️ NumPy (Numerical Python) — Complete Guide with Examples

NumPy is a **powerful Python library** for numerical computing. It provides support for **multi-dimensional arrays**, **mathematical operations**, and **linear algebra**, making it essential for **Data Science, Machine Learning, and AI**.

---

## 🧠 What is NumPy?

**NumPy (Numerical Python)** provides fast and efficient operations for numerical data using **ndarray (N-dimensional array)**.

> NumPy is written in C — it’s much faster than Python lists.

---

## ⚙️ Installation

```bash
pip install numpy
```
Import NumPy:
```python
import numpy as np
```

---

## 🔹 1️⃣ Creating NumPy Arrays

```python
import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5])

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
print(arr2)
```

---

## 🔹 2️⃣ Array Properties

```python
print(arr.ndim)   # Number of dimensions
print(arr.shape)  # Shape (rows, columns)
print(arr.size)   # Total elements
print(arr.dtype)  # Data type
```

---

## 🔹 3️⃣ Creating Special Arrays

```python
np.zeros((2, 3))         # Array of zeros
np.ones((3, 3))          # Array of ones
np.eye(4)                # Identity matrix
np.full((2, 2), 7)       # Filled with a constant
np.arange(0, 10, 2)      # Evenly spaced range
np.linspace(0, 1, 5)     # Equally spaced values
```

---

## 🔹 4️⃣ Data Type Conversion

```python
arr = np.array([1.5, 2.8, 3.6])
print(arr.astype(int))
```

---

## 🔹 5️⃣ Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])
print(arr[-1])

mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat[1, 2])
print(mat[0:2, 1:3])
```

---

## 🔹 6️⃣ Mathematical Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
```

---

## 🔹 7️⃣ Universal Functions (ufuncs)

```python
arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))
print(np.sin(arr))
print(np.cos(arr))
```

---

## 🔹 8️⃣ Aggregation Functions

```python
arr = np.array([10, 20, 30, 40])
print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(np.max(arr))
print(np.min(arr))
```

---

## 🔹 9️⃣ Reshaping Arrays

```python
arr = np.arange(1, 10)
print(arr.reshape(3, 3))
```

---

## 🔹 🔟 Flattening Arrays

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.flatten())
```

---

## 🔹 11️⃣ Stacking Arrays

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))
print(np.hstack((a, b)))
```

---

## 🔹 12️⃣ Splitting Arrays

```python
arr = np.array([10, 20, 30, 40, 50, 60])
print(np.split(arr, 3))
```

---

## 🔹 13️⃣ Boolean Indexing

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25])
```

---

## 🔹 14️⃣ Random Numbers

```python
print(np.random.rand(2, 3))
print(np.random.randint(1, 10, 5))
print(np.random.randn(3))
```

---

## 🔹 15️⃣ Matrix Operations

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)
print(np.dot(A, B))
print(np.transpose(A))
```

---

## 🔹 16️⃣ Broadcasting

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr + 10)
```

---

## 🔹 17️⃣ Copy vs View

```python
arr = np.array([1, 2, 3])
copy_arr = arr.copy()
view_arr = arr.view()

arr[0] = 99

print(copy_arr)  # Independent copy
print(view_arr)  # Shares data
```

---

## 🔹 18️⃣ Sorting and Searching

```python
arr = np.array([3, 1, 4, 1, 5])
print(np.sort(arr))
print(np.where(arr == 4))
print(np.unique(arr))
```

---

## 🔹 19️⃣ Saving and Loading Arrays

```python
arr = np.array([1, 2, 3])
np.save("array.npy", arr)
loaded = np.load("array.npy")
print(loaded)
```

---

## 🔹 20️⃣ Statistical Operations

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr, axis=0))   # Column-wise
print(np.sum(arr, axis=1))   # Row-wise
```

---

## 🧩 NumPy vs Python Lists

| Feature | Python List | NumPy Array |
|----------|--------------|-------------|
| Speed | Slow | 🚀 Fast |
| Memory | High | Low |
| Data Type | Mixed | Homogeneous |
| Math Operations | Manual | Vectorized |
| Use | General | Scientific / ML / AI |

---

## 🧱 Summary

| Concept | Description |
|----------|-------------|
| **Library** | NumPy |
| **Main Object** | ndarray |
| **Core Feature** | Fast numerical computation |
| **Used In** | Data Science, Machine Learning, AI, Image Processing |

---

### ✍️ Author
**Arpan Chakraborty**  
NumPy in Python — Complete Guide with All Operations and Practical Examples.
