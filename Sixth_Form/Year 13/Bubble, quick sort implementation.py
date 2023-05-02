import tkinter as tk
import random
import time
class SortGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sort GUI")

        # Create widgets
        self.label = tk.Label(master, text="Enter up to 100 numbers, separated by spaces:")
        self.entry = tk.Entry(master, width=50)
        self.bubble_button = tk.Button(master, text="Bubble Sort", command=self.bubble_sort)
        self.quick_button = tk.Button(master, text="Quick Sort", command=self.quick_sort)
        self.view_button = tk.Button(master, text="View Passes", command=self.view_passes)
        self.output_label = tk.Label(master, text="")
        self.timer_label = tk.Label(master, text="")

        # Layout widgets
        self.label.grid(row=0, column=0, columnspan=2)
        self.entry.grid(row=1, column=0, columnspan=2)
        self.bubble_button.grid(row=2, column=0)
        self.quick_button.grid(row=2, column=1)
        self.view_button.grid(row=3, column=0)
        self.output_label.grid(row=4, column=0, columnspan=2)
        self.timer_label.grid(row=5, column=0, columnspan=2)

        # Initialize variables
        self.numbers = []
        self.passes = []

    def bubble_sort(self):
        pass

    def quick_sort(self):
        pass

    def view_passes(self):
        pass
def main():
    root = tk.Tk()
    gui = SortGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
