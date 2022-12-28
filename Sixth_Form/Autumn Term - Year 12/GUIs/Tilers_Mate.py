from tkinter import *
import math

root = Tk()
root.title('Tilers_Mate')
root.geometry("500x500")


def user_click_width_floor():
    try:
        int(width_floor_entry.get())
        verified_width_floor.config(text="Number √")
    except ValueError:
        verified_width_floor.config(text="not a number ×")


width_floor = Label(root, text="Enter the Width of the Floor")
width_floor.pack(pady=3)

width_floor_entry = Entry(root)
width_floor_entry.pack(pady=3)

verify_button_width_floor = Button(root, text="Verify", command=user_click_width_floor)
verify_button_width_floor.pack(pady=3)

verified_width_floor = Label(root, text='')
verified_width_floor.pack(pady=3)


def user_click_length_floor():
    try:
        int(length_floor_entry.get())
        verified_length_floor.config(text="Number √")
    except ValueError:
        verified_length_floor.config(text="not a number × ")


length_floor = Label(root, text="Enter the Length of the floor")
length_floor.pack(pady=3)

length_floor_entry = Entry(root)
length_floor_entry.pack(pady=3)

verify_button_length_floor = Button(root, text="Verify", command=user_click_length_floor)
verify_button_length_floor.pack(pady=3)

verified_length_floor = Label(root, text='')
verified_length_floor.pack(pady=3)


def user_click_width_tile():
    try:
        int(width_tile_entry.get())
        verified_width_tile.config(text="Number √")
    except ValueError:
        verified_width_tile.config(text="not a number ×")


width_tile = Label(root, text="Enter the Width of the Tile")
width_tile.pack(pady=3)

width_tile_entry = Entry(root)
width_tile_entry.pack(pady=3)

verify_button_width_tile = Button(root, text="Verify", command=user_click_width_tile)
verify_button_width_tile.pack(pady=3)

verified_width_tile = Label(root, text='')
verified_width_tile.pack(pady=3)


def user_click_length_tile():
    try:
        int(length_tile_entry.get())
        verified_length_tile.config(text="Number √")
    except ValueError:
        verified_length_tile.config(text="not a number × ")


length_tile = Label(root, text="Enter the Length of the Tile")
length_tile.pack(pady=3)

length_tile_entry = Entry(root)
length_tile_entry.pack(pady=3)

verify_button_length_tile = Button(root, text="Verify", command=user_click_length_tile)
verify_button_length_tile.pack(pady=3)

verified_length_tile = Label(root, text='')
verified_length_tile.pack(pady=3)


def user_click_cost_tile():
    try:
        int(cost_tile_entry.get())
        verified_cost_tile.config(text="Number √")
    except ValueError:
        verified_cost_tile.config(text="not a number × ")


cost_tile = Label(root, text="Enter the Cost of the Tile")
cost_tile.pack(pady=3)

cost_tile_entry = Entry(root)
cost_tile_entry.pack(pady=3)

verify_button_cost_tile = Button(root, text="Verify", command=user_click_cost_tile)
verify_button_cost_tile.pack(pady=3)

verified_cost_tile = Label(root, text='')
verified_cost_tile.pack(pady=3)

cost_total = Label(root, text="The Total Cost of The Floor Will Be")
cost_total.pack(pady=3)
cost_total_calculation = Label(root, text="put: ((Length_floor × Width_floor) ÷ (Length_tile × Width_tile)) × cost_tile"
                                          " into calculator")
cost_total_calculation.pack(pady=3)

root.mainloop()
