import tkinter as tk

root = tk.Tk()
var1 = tk.IntVar()
check1 = tk.Checkbutton(root, text="Label 1", variable=var1)


def print_selected_labels():
    selected_labels = []
    if var1.get() == 1:
        selected_labels.append("Label 1")
    print("Selected labels:", selected_labels)


ok_button = tk.Button(root, text="Ok", command=print_selected_labels)
check1.grid(row=0, column=1)
ok_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
