from tkinter import *

unit_dict = {
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams": 1.0,
    "kg": 1000.0,
    "tonnes": 1000000.0,
    "pounds": 453.592,
    "square m": 1.0,
    "square km": 1000000.0,
    "square mile": 2590000.0,
    "square foot": 0.0929,
    "Litre": 1.0,
    "ml": 0.001,
    "gallon": 3.785
}

lengths = ["cm", "m", "km", "feet", "miles", "inches", ]
weights = ["kg", "grams", "tonnes", "pounds", ]
temps = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km", "sq. mile", "sq. foot"]
volumes = ["Litre", "ml", "gallon"]


OPTIONS = ["Select Units",
           "cm",
           "m",
           "km",
           "feet",
           "miles",
           "inches",
           "kg",
           "grams",
           "tonnes",
           "pounds",
           "Celsius",
           "Fahrenheit",
           "square m",
           "square km",
           "square mile",
           "square foot",
           "Litre",
           "ml",
           "gallon"]

root = Tk()
root.geometry("400x350")
root.title("Unit Converter")
root['bg'] = 'royal blue'


def ok():
    inp = float(input_entry.get())
    inp_unit = inputopt.get()
    out_unit = outputopt.get()

    cons = [inp_unit in lengths and out_unit in lengths,
            inp_unit in weights and out_unit in weights,
            inp_unit in temps and out_unit in temps,
            inp_unit in areas and out_unit in areas,
            inp_unit in volumes and out_unit in volumes]

    if any(cons):
        if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            output_entry.delete(0, END)
            output_entry.insert(0, (inp * 1.8) + 32)
        elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            output_entry.delete(0, END)
            output_entry.insert(0, (inp - 32) * (5 / 9))
        else:
            output_entry.delete(0, END)
            output_entry.insert(0, round(inp * unit_dict[inp_unit] / unit_dict[out_unit], 5))

    else:
        output_entry.delete(0, END)
        output_entry.insert(0, "ERROR")


inputopt = StringVar()
inputopt.set(OPTIONS[0])

outputopt = StringVar()
outputopt.set(OPTIONS[0])


input_label = Label(root, text="Starting Measurement")
input_label.grid(row=0, column=0, pady=20)

input_entry = Entry(root, justify="center", font="bold")
input_entry.grid(row=1, column=0, padx=35, ipady=5)

input_menu = OptionMenu(root, inputopt, *OPTIONS)
input_menu.grid(row=1, column=1)
input_menu.config(font="Helevetica 10")

output_label = Label(root, text="Converted Measurement")
output_label.grid(row=2, column=0, pady=20)

output_entry = Entry(root, justify="center", font="bold")
output_entry.grid(row=3, column=0, padx=35, ipady=5)

output_menu = OptionMenu(root, outputopt, *OPTIONS)
output_menu.grid(row=3, column=1)
output_menu.config(font="Helevetica 10")

ok_btn = Button(root, text="OK", command=ok, padx=80, pady=2)
ok_btn.grid(row=4, column=0, columnspan=3, pady=50)

root.mainloop()
