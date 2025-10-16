#!/usr/bin/env python3

"""
Manages the main application window.
Python 3.13+
Date created: October 10th, 2025
Date modified: -
"""

import logging
from logging.config import fileConfig

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

from src import error_window
from src import about_window
from src import input_password

fileConfig("logging.ini")
logger = logging.getLogger()


class MainWindow:
    """
    Manages the main application window for a file encryption and decryption utility.

    This class is responsible for setting up the graphical user interface (GUI) for the encryption and decryption application. It provides features to select a file, encrypt or decrypt the file using AES encryption with a user-provided key.
    """

    def __init__(self, app_window: tk.Tk):
        self.window = app_window
        self.window.lift()  # Brings the window to the front

        self.window.title("Arcanum")

        # Customize macOS menu bar (optional)
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)

        # Add "File" with "Quit" button to menu bar.
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Quit", command=self.window.quit)

        window_width = 600
        window_height = 300

        # Get the screen dimension
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # Set the position of the window to the center of the screen
        self.window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        # Window is resizable?
        self.window.resizable(False, False)

        self.selected_file = None

        # Create input frame
        self.input_frame = ttk.Frame(self.window, padding=(10, 10, 10, 10))
        self.input_frame.grid(row=0, column=0, sticky="nsew")

        # Add a button to select a file
        self.file_button = ttk.Button(
            self.input_frame, text="Select file", command=self.on_button_clicked
        )
        self.file_button.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # Add a label to display the selected file
        self.file_label = ttk.Label(
            self.input_frame, text="Click on the button to select a file"
        )
        self.file_label.grid(row=1, column=0, sticky="w", padx=10)

        # Create a first button frame
        self.button_frame_one = ttk.Frame(self.window, padding=(10, 10, 10, 10))
        self.button_frame_one.grid(row=1, column=0, sticky="nsew")

        # Add buttons for encryption and decryption
        self.encrypt_button = ttk.Button(
            self.button_frame_one,
            text="Encrypt",
            command=self.on_encrypt_clicked,
            state=tk.DISABLED,
        )
        self.encrypt_button.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.decrypt_button = ttk.Button(
            self.button_frame_one,
            text="Decrypt",
            command=self.on_decrypt_clicked,
            state=tk.DISABLED,
        )
        self.decrypt_button.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        # Create a second button frame
        self.button_frame_two = ttk.Frame(self.window, padding=(10, 10, 10, 10))
        self.button_frame_two.grid(row=2, column=0, sticky="sw")

        # Add a button to quit the application
        self.quit_button = ttk.Button(
            self.button_frame_two, text="Quit", command=self.quit_program
        )
        self.quit_button.grid(row=0, column=0, sticky="sw", padx=10, pady=80)

        # Add a button to show the about window
        self.about_button = ttk.Button(
            self.button_frame_two,
            text="About",
            command=lambda: about_window.show_custom_about(),
        )
        self.about_button.grid(row=0, column=1, sticky="w")

        # Add weight to the grid layout
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.button_frame_one.grid_rowconfigure(0, weight=1)
        self.button_frame_one.grid_columnconfigure(1, weight=1)
        self.button_frame_two.grid_columnconfigure(0, weight=1)

    def on_button_clicked(self):
        """
        Handles the event when a button is clicked to select a file. The function opens a dialog to select a file, updates the selected file's path to the label and enables encrypt and decrypt buttons.

        Raises:
            None
        """
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Encrypted files", "*.enc")]
        )
        if file_path:
            self.selected_file = file_path
            self.file_label.config(text=f"Selected file: {self.selected_file}")

        self.encrypt_button.config(state=tk.NORMAL)
        self.decrypt_button.config(state=tk.NORMAL)

    def on_encrypt_clicked(self):
        """
        Handles the encryption operation when the button 'encrypt' is clicked. It encrypts the contents of a selected file using AES encryption with a randomly generated IV (Initialization Vector) in CFB mode and writes the encrypted data to a new file with a `.enc` extension.

        Raises:
            None
        """
        if self.selected_file:
            password = input_password.get_password()
            if password is None:
                return

            with open(self.selected_file, "rb") as f:
                data = f.read()

            salt = get_random_bytes(16)
            iv = get_random_bytes(16)
            key = PBKDF2(password, salt, dkLen=32)

            cipher = AES.new(key, AES.MODE_CFB, iv=iv)
            encrypted_data = salt + iv + cipher.encrypt(data)

            # Append `.enc` so you can identify encrypted files
            enc_file_path = self.selected_file + ".enc"

            with open(enc_file_path, "wb") as f:
                f.write(encrypted_data)
            self.file_label.config(text=f"File encrypted: {enc_file_path}")

    def on_decrypt_clicked(self):
        """
        Handles the decryption of an encrypted file when the decrypt button is clicked. It verifies that the selected file has the correct extension, retrieves the encryption key, decrypts the file content and saves the decrypted file with its original name.

        Raises:
            None
        """
        if self.selected_file and self.selected_file.endswith(".enc"):
            password = input_password.get_password()
            if password is None:
                return

            with open(self.selected_file, "rb") as f:
                encrypted_data = f.read()

            retrieved_salt = encrypted_data[:16]
            retrieved_iv = encrypted_data[16:32]
            retrieved_ciphertext = encrypted_data[32:]

            key = PBKDF2(password, retrieved_salt, dkLen=32)
            cipher = AES.new(key, AES.MODE_CFB, iv=retrieved_iv)
            decrypted_data = cipher.decrypt(retrieved_ciphertext)

            # Remove the `.enc` extension to get the original filename
            dec_file_path = self.selected_file.rsplit(".enc", 1)[0]
            with open(dec_file_path, "wb") as f:
                f.write(decrypted_data)
            self.file_label.config(text=f"File decrypted: {dec_file_path}")

        else:
            error_window.show_error("Not an encrypted file.")

    def quit_program(self):
        """
        Destroys the main application window.

        This method is used to terminate the application by closing the primary window. It leverages the `destroy` method of the `tkinter` library to shut down the interface and safely exit the program.

        Raises:
            None
        """
        self.window.destroy()

    def mainloop(self):
        """
        Executes the main event loop for the graphical user interface (GUI).

        This method is responsible for starting the tkinter event loop, which continually listens for and processes user input such as mouse clicks or keypresses within the application window. The loop runs until the application window is closed.

        Returns:
            None
        """
        self.window.mainloop()
