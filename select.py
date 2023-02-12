import os

def select_file():
    print("1. Select file using explorer")
    print("2. Enter file path manually")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            if file_path:
                return file_path
            else:
                print("No file selected.")
                return None
        except ImportError:
            print("tkinter module not found.")
            return None
    elif choice == "2":
        file_path = input("Enter file path: ")
        if os.path.isfile(file_path):
            return file_path
        else:
            print("File not found.")
            return None
    elif choice == "3":
        return None
    else:
        print("Invalid choice.")
        return None

file_path = select_file()
if file_path:
    with open(file_path) as f:
        print("Content of the selected file:")
        print(f.read())
else:
    print("Exiting the program.")
