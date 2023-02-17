import tkinter as tk

# Create a Tkinter window
root = tk.Tk()

# Create a Canvas widget
canvas = tk.Canvas(root, width=200, height=200, bg='white')
canvas.pack()

# Create some buttons and labels inside the Canvas
button1 = tk.Button(canvas, text="Button 1")
button1_window = canvas.create_window(40, 50, window=button1)
label1 = tk.Label(canvas, text="Label 1")
label1_window = canvas.create_window(40, 80, window=label1)
button2 = tk.Button(canvas, text="Button 2")
button2_window = canvas.create_window(40, 110, window=button2)
label2 = tk.Label(canvas, text="Label 2")
label2_window = canvas.create_window(40, 140, window=label2)

# Create a blue outline around the widgets
x1, y1, x2, y2 = canvas.bbox("all")
canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=2)

# Run the Tkinter event loop
root.mainloop()
