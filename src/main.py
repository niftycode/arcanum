#!/usr/bin/env python3

"""
A simple and secure file encryption and decryption utility.
Version: 1.0
Python 3.13+
Date created: October 10th, 2025
Date modified: October 15th, 2025
"""


import tkinter as tk

from src import window_manager


def main():
    """
    Main entry point of the application.

    This function initializes the main tkinter window, sets up the
    main window using the window manager, and starts the application's
    main event loop.
    """
    window = tk.Tk()
    main_window = window_manager.MainWindow(window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
