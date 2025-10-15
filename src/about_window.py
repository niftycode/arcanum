#!/usr/bin/env python3

"""
Version: 1.0
Python 3.13+
Date created: October 15th, 2025
Date modified: -
"""

import tkinter as tk

from tkinter import ttk


def show_custom_about():
    about = tk.Toplevel()
    about.title("About this app")
    about.resizable(False, False)

    window_width = 300
    window_height = 260

    # Get the screen dimension
    screen_width = about.winfo_screenwidth()
    screen_height = about.winfo_screenheight()
    # Find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    # Set the position of the window to the center of the screen
    about.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    # App name
    tk.Label(about, text="Arcanum", font=("Helvetica", 16, "bold")).pack(pady=(10, 0))

    # Version
    tk.Label(about, text="Version 0.1.0").pack()

    # Copyright
    tk.Label(about, text="2025 MIT License").pack(pady=(0, 10))

    # Separator
    ttk.Separator(about, orient="horizontal").pack(fill="x", padx=10)

    # Description
    description = tk.Label(
        about,
        text="A simple and secure file encryption\nand decryption utility with\na graphical user interface built\nusing Python and Tkinter.\n\n"
        "Created by niftycode",
        justify="center",
    )
    description.pack(pady=10)

    # OK button
    ttk.Button(about, text="OK", command=about.destroy).pack(pady=(0, 10))
