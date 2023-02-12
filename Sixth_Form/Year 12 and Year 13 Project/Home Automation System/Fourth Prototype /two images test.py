import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


def create_second_window():
    second_window = tk.Toplevel()
    second_window.title("Second Window")

    # Load the image
    image = PhotoImage(file="first.png")

    # Create a label and display the image on it
    label = tk.Label(second_window, image=image)
    label.pack()


root = tk.Tk()
root.title("Main Window")

# Create a button to open the second window
button = ttk.Button(root, text="Open Second Window", command=create_second_window)
button.pack()

root.mainloop()

