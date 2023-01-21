from tkinter import *
import emoji

test_window = Tk()
test_window.title('A Level Computer Science Project')
test_window.geometry("450x300")
email_address_entry = Entry(test_window)
email_address_entry.place(x=150, y=70)
email_address_text = Label(test_window, text="Email address")
email_address_text.place(x=56.2, y=72)
check_clause_2_email_address = Label(test_window, text="'@' sign")
check_clause_2_email_address.place(x=150, y=110)
check_clause_1_email_address_cross_emoji = Label(test_window, text=f'{emoji.emojize(":cross_mark:")}')
check_clause_1_email_address_cross_emoji.place(x=125, y=110)
check_clause_1_email_address_tick_emoji = Label(test_window, text=f'{emoji.emojize(":check_mark_button:")}')
check_clause_1_email_address_tick_emoji.place(x=100, y=110)
test_window.resizable(False, False)
test_window.mainloop()
