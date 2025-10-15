# Python File Operations

File operations allow Python programs to **read, write, and manipulate files** on your computer. Files can be of types like text (`.txt`), CSV (`.csv`), JSON (`.json`), or binary files (`.bin`, images, etc.).  

Python provides the built-in `open()` function to work with files.

---

## 1. Opening a File

```python
file_object = open("filename", "mode")
```

# Modes of File Opening
```
Mode	Description
r	Read (default) – file must exist
w	Write – creates a file or truncates if exists
a	Append – add content at the end of file
x	Exclusive creation – fails if file exists
rb	Read binary
wb	Write binary
ab	Append binary
r+	Read and write
w+	Write and read (overwrite)
a+	Append and read
```
## 2. Reading Files
## Read the whole file
```
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```
## Read line by line
```
file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()
```
## Read specific number of characters
```
file = open("example.txt", "r")
print(file.read(10))  # Read first 10 characters
file.close()
```
## 3. Writing Files
## Write (overwrite) a file
```
file = open("example.txt", "w")
file.write("Hello World!\n")
file.write("Python File Operations.")
file.close()
```
## Append to a file
```
file = open("example.txt", "a")
file.write("\nThis line is appended.")
file.close()
```
## 4. Using with Statement (Recommended)

## Using with automatically closes the file after operations:
```
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
## 5. File Pointer and seek()
```
with open("example.txt", "r") as file:
    print(file.read(5))  # Reads first 5 characters
    file.seek(0)         # Move pointer to beginning
    print(file.read())   # Reads entire content
```
## 6. Reading and Writing Binary Files
## Reading an image
```
with open("image.jpg", "rb") as img:
    data = img.read()
    print(type(data))  # <class 'bytes'>
```
## Writing an image
```
with open("copy.jpg", "wb") as img_copy:
    img_copy.write(data)
```
## 7. Checking if a File Exists
```
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")
```
## 8. Deleting a File
```
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted")
else:
    print("File not found")
```
## 9. Summary of File Operations
```
Open a file using open().

Read/Write/Append depending on mode.

Close the file using close() or with.

Binary files use rb, wb, ab.

File pointer can be moved with seek().

Check and delete files with os module.
```
## Tips:
```
Always prefer with statement to avoid forgetting close().

For large files, read line by line instead of reading all at once.

Use binary mode for non-text files.
```