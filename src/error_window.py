#!/usr/bin/env python3

"""
Displays an error message in a modal dialog box.
Python 3.13+
Date created: October 15th, 2025
Date modified: -
"""

import tkinter as tk
from tkinter import messagebox


def show_error(message: str):
    """
    Displays an error message in a modal dialog box.

    This function creates a temporary, hidden root window to display an
    error message using the tkinter `messagebox` module. After the
    dialog is shown, the root window is destroyed to clean up resources.

    Args:
        message (str): The error message to be displayed in the dialog box.
    """
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.destroy()
