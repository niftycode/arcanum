# arcanum

A simple and secure file encryption and decryption utility with a graphical user interface built using Python and Tkinter.

## Overview

Arcanum is a desktop application that allows users to easily encrypt and decrypt files using AES (Advanced Encryption Standard) encryption. The application features a user-friendly GUI that simplifies the process of protecting sensitive files with password-based encryption.

## Features

- **AES Encryption**: Uses AES encryption in CFB (Cipher Feedback) mode
- **Password-Based Key Derivation**: Implements PBKDF2 for secure key generation from user passwords
- **User-Friendly GUI**: Simple Tkinter-based interface for easy file selection and operations
- **File Type Support**: Works with text files
- **Compatible with macOS**

## Requirements

- Python 3.13 or higher
- Dependencies (automatically installed via `pip` or `pip3`):
  - pycryptodome

Dependencies can be installed using

```Bash
pip3 install -r requirements.txt
```

## Installation

1. Clone the repository
2. Create a virtual environment
2. Use `pip3` to install the dependencies
3. Run the main.py file
