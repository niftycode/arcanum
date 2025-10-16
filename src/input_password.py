#!/usr/bin/env python3

"""
This module contains utilities for generating a cryptographic key for encryption or decryption purposes.
Python 3.13+
Date created: October 16th, 2025
Date modified: -
"""

from tkinter import messagebox, simpledialog


from typing import Optional


def get_password() -> Optional[str]:
    """
    Prompts the user to input a secret key securely.

    The function displays a dialog box where the user can enter their secret key.
    If the user cancels the prompt or does not provide input, a warning message
    is displayed and the function returns None. Otherwise, it returns the entered
    secret key.

    Returns:
        str: The secret key entered by the user, or None if no input is provided.
    """
    password = simpledialog.askstring("Input", "Enter secret key:", show="*")
    if not password:
        messagebox.showwarning("Warning", "Missing Secret Key")
        return None

    return password
