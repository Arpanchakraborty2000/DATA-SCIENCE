# File Paths in Python

A **file path** is a string that specifies the location of a file or directory on your computer. Python allows you to work with **absolute paths** and **relative paths** to access files.

---

## 1. Absolute Path

An absolute path specifies the **full location** of the file from the root directory.

**Example (macOS/Linux):**
```python
file_path = "/Users/arpan/Documents/example.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
```
Example (Windows):
```python
file_path = "C:\\Users\\Arpan\\Documents\\example.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
```

Note: In Windows, you can also use raw strings to avoid double backslashes:
```python
file_path = r"C:\Users\Arpan\Documents\example.txt"
```
## 2. Relative Path

A relative path is relative to the current working directory of the Python script.

File in the same directory as script:
```python
file_path = "example.txt"

with open(file_path, "r") as file:
    print(file.read())
```

Example with subdirectories:
```python
file_path = "data/input.txt"  # file inside 'data' folder
with open(file_path, "r") as file:
    print(file.read())
```
## 3. Current Working Directory

You can find or change the current working directory using the os module:
```python
import os

# Get current directory
cwd = os.getcwd()
print("Current Directory:", cwd)

# Change directory
os.chdir("/Users/arpan/Documents")
print("Changed Directory:", os.getcwd())
```
## 4. Path Operations using os.path

Python provides the os.path module to manipulate paths.
```python
import os

file_path = "/Users/arpan/Documents/example.txt"

# Check if file exists
print(os.path.exists(file_path))  # True or False

# Get directory name
print(os.path.dirname(file_path))  # /Users/arpan/Documents

# Get file name
print(os.path.basename(file_path))  # example.txt

# Join paths
new_path = os.path.join("/Users/arpan/Documents", "newfile.txt")
print(new_path)
```
## 5. Using pathlib (Recommended)

Python 3.4+ introduced pathlib, a modern way to handle paths:
```python
from pathlib import Path

# Absolute path
file_path = Path("/Users/arpan/Documents/example.txt")
print(file_path.exists())

# Relative path
file_path = Path("data/input.txt")
print(file_path.exists())

# Join paths
new_path = Path("/Users/arpan/Documents") / "newfile.txt"
print(new_path)

# Get parent directory
print(file_path.parent)

# Get file name
print(file_path.name)
```
## 6. Special Paths

. → Current directory

.. → Parent directory
```python
# File in parent directory
file_path = "../example.txt"

# File in current directory
file_path = "./example.txt"
```
## 7. Examples of Opening Files Using Different Paths

Absolute path:
```python
with open("/Users/arpan/Documents/example.txt", "r") as f:
    print(f.read())
```

Relative path (subdirectory):
```python
with open("data/input.txt", "r") as f:
    print(f.read())
```

Using pathlib:
```python
from pathlib import Path

file = Path("data/input.txt")
with file.open("r") as f:
    print(f.read())
```
## ✅ Summary

Absolute path: Full path from root.

Relative path: Relative to current working directory.

os.path and pathlib: Used for path manipulations.

Special symbols: . → current, .. → parent.

Always prefer pathlib in modern Python for clarity and cross-platform compatibility.