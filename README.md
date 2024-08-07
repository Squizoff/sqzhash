# SqzHash

SqzHash is a simple yet reliable 256-bit cryptographic hash algorithm designed for efficient computation of hash values. It employs shifts, XOR operations, and prime numbers to ensure robust hashing capabilities. SqzHash processes data in chunks, continuously updating its state to generate unique hash sums for strings and files, making it suitable for a wide range of applications.

## Installation

You can install SqzHash using pip:

```sh
pip install sqzhash
```

# Example Usage
## Hashing a String
You can use the hash_string function to compute the hash of a string.
```python
from sqzhash import hash_string

input_string = "example string"
hash_value = hash_string(input_string)
print(f"Hash value for the string is: {hash_value}")
```

## Hashing a File
You can use the hash_file function to compute the hash of a file.
```python
from sqzhash import hash_file

file_path = "path/to/your/file.txt"
hash_value = hash_file(file_path)
print(f"Hash value for the file is: {hash_value}")
```