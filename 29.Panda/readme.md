# 🐼 Pandas (Python Data Analysis Library) — Complete Guide with Examples and Outputs

Pandas is a **powerful open-source library** used for **data analysis, manipulation, and cleaning** in Python.  
It provides two main data structures: **Series** and **DataFrame**, which make working with structured data easy and efficient.

---

## ⚙️ Installation

```bash
pip install pandas
```

Import Pandas:
```python
import pandas as pd
```

---

## 🧠 What is Pandas?

Pandas allows you to work with tabular data (like Excel or SQL tables) using Python.  
It’s built on **NumPy** and is used for:
- Reading and writing data (CSV, Excel, SQL, JSON, etc.)
- Data cleaning and manipulation
- Filtering and grouping
- Statistical analysis

---

## 🧩 Pandas Data Structures

| Structure | Description | Example |
|------------|--------------|----------|
| **Series** | 1D labeled array | Single column |
| **DataFrame** | 2D labeled table | Rows & columns like Excel |

---

## ✅ 1️⃣ Creating a Series

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```
🧾 **Output:**
```
0    10
1    20
2    30
3    40
dtype: int64
```

---

## ✅ 2️⃣ Creating a DataFrame

```python
data = {
    "Name": ["Arpan", "Sreya", "Rohan"],
    "Age": [25, 23, 27],
    "City": ["Kolkata", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)
```
🧾 **Output:**
```
    Name  Age     City
0  Arpan   25  Kolkata
1  Sreya   23    Delhi
2  Rohan   27   Mumbai
```

---

## ✅ 3️⃣ Viewing Data

```python
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
```

---

## ✅ 4️⃣ Selecting Columns & Rows

```python
print(df["Name"])          # Single column
print(df[["Name", "Age"]]) # Multiple columns
print(df.iloc[0])          # Row by index
print(df.loc[1])           # Row by label
```

---

## ✅ 5️⃣ Filtering Rows

```python
print(df[df["Age"] > 24])
```
🧾 **Output:**
```
    Name  Age     City
0  Arpan   25  Kolkata
2  Rohan   27   Mumbai
```

---

## ✅ 6️⃣ Adding / Modifying Columns

```python
df["Salary"] = [60000, 55000, 70000]
df["Bonus"] = df["Salary"] * 0.1
print(df)
```

🧾 **Output:**
```
    Name  Age     City  Salary   Bonus
0  Arpan   25  Kolkata   60000  6000.0
1  Sreya   23    Delhi   55000  5500.0
2  Rohan   27   Mumbai   70000  7000.0
```

---

## ✅ 7️⃣ Sorting

```python
print(df.sort_values(by="Age", ascending=False))
```

---

## ✅ 8️⃣ Grouping Data

```python
data = {
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 55000, 42000]
}
df2 = pd.DataFrame(data)
print(df2.groupby("Department")["Salary"].mean())
```
🧾 **Output:**
```
Department
HR    41000.0
IT    52500.0
Name: Salary, dtype: float64
```

---

## ✅ 9️⃣ Handling Missing Data

```python
data = {
    "Name": ["A", "B", "C"],
    "Age": [20, None, 25]
}
df3 = pd.DataFrame(data)
df3["Age"].fillna(0, inplace=True)
print(df3)
```

🧾 **Output:**
```
  Name   Age
0    A  20.0
1    B   0.0
2    C  25.0
```

---

## ✅ 🔟 Removing Duplicates

```python
df = pd.DataFrame({"Name": ["A", "A", "B"], "Age": [25, 25, 30]})
df.drop_duplicates(inplace=True)
print(df)
```

---

## ✅ 11️⃣ Combining DataFrames

```python
df1 = pd.DataFrame({"Name": ["A", "B"], "Age": [20, 21]})
df2 = pd.DataFrame({"Name": ["C", "D"], "Age": [22, 23]})
combined = pd.concat([df1, df2])
print(combined)
```

---

## ✅ 12️⃣ Merging DataFrames

```python
df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Arpan", "Sreya", "Rohan"]})
df2 = pd.DataFrame({"ID": [1, 2, 3], "City": ["Kolkata", "Delhi", "Mumbai"]})

merged = pd.merge(df1, df2, on="ID")
print(merged)
```

🧾 **Output:**
```
   ID    Name     City
0   1   Arpan  Kolkata
1   2   Sreya    Delhi
2   3   Rohan   Mumbai
```

---

## ✅ 13️⃣ Rename Columns

```python
df.rename(columns={"Age": "Years"}, inplace=True)
print(df)
```

---

## ✅ 14️⃣ Apply Custom Function

```python
def category(age):
    return "Adult" if age >= 25 else "Young"

df["Category"] = df["Years"].apply(category)
print(df)
```

---

## ✅ 15️⃣ Reading & Writing Excel Files

```python
df.to_excel("output.xlsx", index=False)
df2 = pd.read_excel("output.xlsx")
print(df2)
```

---

## ✅ 16️⃣ Plotting with Pandas

```python
import matplotlib.pyplot as plt

df["Years"].plot(kind="bar", title="Age Distribution")
plt.xlabel("Index")
plt.ylabel("Years")
plt.show()
```

---

## ✅ 17️⃣ String Operations

```python
df["Name"] = df["Name"].str.upper()
print(df)
```

---

## ✅ 18️⃣ Conditional Column Creation

```python
df["Level"] = ["Senior" if age > 30 else "Junior" for age in df["Years"]]
print(df)
```

---

## 🧾 Common Pandas Operations Summary

| Operation | Description | Example |
|------------|-------------|----------|
| `read_csv()` | Read CSV file | `pd.read_csv("file.csv")` |
| `to_csv()` | Save DataFrame | `df.to_csv("out.csv")` |
| `head()` | Show top rows | `df.head()` |
| `groupby()` | Aggregate data | `df.groupby("Dept").mean()` |
| `fillna()` | Replace missing | `df.fillna(0)` |
| `drop()` | Remove column | `df.drop("col", axis=1)` |
| `merge()` | Merge DataFrames | `pd.merge(df1, df2)` |
| `concat()` | Stack vertically | `pd.concat([df1, df2])` |

---

## 🧱 Summary

| Concept | Description |
|----------|-------------|
| **Library Name** | Pandas |
| **Main Structures** | Series, DataFrame |
| **Use Case** | Data analysis, cleaning, visualization |
| **Built On** | NumPy |
| **Common Uses** | ML preprocessing, ETL, analytics |

---

### ✍️ Author
**Arpan Chakraborty**  
Pandas in Python — Complete Guide with All Operations and Practical Examples.
