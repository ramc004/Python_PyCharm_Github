import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from random import randint


def create_widgets():
    style = ttk.Style()
    style.configure("TLabel", font=("", 16))
    style.configure("TButton", font=("", 16))


class FizzBuzzGame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.fizzbuzz_button = ttk.Button(self, text="FizzBuzz",
                                          command=lambda: self.button_clicked(clicked="fizzbuzz"))
        self.buzz_button = ttk.Button(self, text="Buzz", command=lambda: self.button_clicked(clicked="buzz"))
        self.fizz_button = ttk.Button(self, text="Fizz", command=lambda: self.button_clicked(clicked="fizz"))
        self.number_label = ttk.Label(self, text="Number: " + str(self.number))
        self.timer_label = ttk.Label(self, text="Time: " + str(self.timer))
        self.timer_bar = ttk.Progressbar(self)
        self.score_label = ttk.Label(self, text="Score: " + str(self.score))
        self.timer_bar_step_size = 99.99 / self.timer
        self.timer = 30
        self.number = 0
        self.score = 0
        self.title("FizzBuzz Game")
        self.resizable(0, 0)
        self.declare_variables()
        create_widgets()
        self.show_welcome_message()
        self.new_number()
        self.game_timer()

    def declare_variables(self):
        pass

    def show_welcome_message(self):
        message = "Welcome to the FizzBuzz Game! You'll have %d seconds to get the highest score you can. " \
                  % self.timer + \
                  "If a number is divisible by 3, click Fizz. If it's divisible by 5, click Buzz. " + \
                  "If it's divisible by both, click FizzBuzz! Click OK to begin. Good luck!"

        messagebox.showinfo("FizzBuzz Game", message)

    def new_number(self):
        random_number = randint(3, 99)
        if (random_number % 3 != 0) and (random_number % 5 != 0):
            self.new_number()
        else:
            self.number = random_number
            self.number_label.config(text="Number: " + str(self.number))

    def game_timer(self):
        self.timer -= 1
        self.timer_label.config(text="Time: " + str(self.timer))
        self.timer_bar.step(-self.timer_bar_step_size)

        if self.timer != 0:
            self.after(1000, self.game_timer)
        else:
            messagebox.showinfo("FizzBuzz Game", "Time's up! Your final score is %d." % self.score)
            quit()

    def button_clicked(self, clicked=None):
        answer = "fizzbuzz" if self.number % 15 == 0 \
            else "buzz" if self.number % 5 == 0 \
            else "fizz"

        if answer == clicked:
            self.score += 1
            self.score_label.config(text="Score: " + str(self.score), foreground="green")
        else:
            if self.score == 0:
                pass
            else:
                self.score -= 1
            self.score_label.config(text="Score: " + str(self.score), foreground="red")

        self.new_number()


if __name__ == "__main__":
    game = FizzBuzzGame()
    game.mainloop()
