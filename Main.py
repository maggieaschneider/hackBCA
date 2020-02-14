from tkinter import *
# from academy import academy
# from aesthetic import aesthetic
# from Basic_calc import Basic_calc
# from calendar import calendar
# from click_counter import click_counter
# from color_change import color_change
# from color_person import color_person
# from disney_princess import disney_princess
# from emoji_gen import emoji_gen
# from font_change import font_change
# from hogwarts_house import hogwarts_house
# from mad_lib import mad_lib
# from mean_median import mean_median
# from meme_gen import meme_gen
# from menu import menu
# from Periodic_table import Periodic_table
# from rand_num_gen import rand_num_gen
# from spirit_animal import spirit_animal
# from surprise import surprise
# from third_grade_quiz import third_grade_quiz
# from wallet import wallet
# from workout_exercise import workout_exercise
# from zodiac_sign import zodiac_sign


class Main(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "WELCOME TO L-CARM!")
        Button(self, text = "Basic Calculations", font = "Helvetica 10", command = self.Basic_calc
               ).grid(row = 2, column = 0)
        Button(self, text = "Calendar", font= "Helvetica 10", command = self.calendar
               ).grid(row=3, column = 1)
        Button(self, text = "Click Counter", font= "Helvetica 10", command = self.click_counter
               ).grid(row=2, column = 2)
        Button(self, text="Text Color Change", font="Helvetica 10", command=self.color_change
               ).grid(row=3, column=3)
        Button(self, text="Text Font Change", font="Helvetica 10", command=self.font_change
               ).grid(row=2, column=4)
        Button(self, text="Emoji Generator", font="Helvetica 10", command=self.emoji_gen
               ).grid(row=2, column=5)
        Button(self, text="Mad Lib", font="Helvetica 10", command=self.mad_lib
               ).grid(row=3, column=6)
        Button(self, text="Mean & Median", font="Helvetica 10", command=self.mean_median
               ).grid(row=2, column=7)
        Button(self, text="CS Meme Generator", font="Helvetica 10", command=self.meme_gen
               ).grid(row=3, column=8)
        Button(self, text="Menu Total", font="Helvetica 10", command=self.menu
               ).grid(row=2, column=9)
        Button(self, text="Periodic Table", font="Helvetica 10", command=self.Periodic_table
               ).grid(row=3, column=10)
        Button(self, text="Random Number Generator", font="Helvetica 10", command=self.rand_num_gen
               ).grid(row=2, column=11)
        Button(self, text="Third Grade Quiz", font="Helvetica 10", command=self.third_grade_quiz
               ).grid(row=3, column=12)
        Button(self, text="Wallet", font="Helvetica 10", command=self.wallet
               ).grid(row=2, column=13)
        Button(self, text="Exercise Suggestion", font="Helvetica 10", command=self.workout_exercise
               ).grid(row=3, column=14)
        Button(self, text="Surprise!!", font="Helvetica 10", command=self.surprise
               ).grid(row=2, column=15)
root = Tk()
root.title("Main screen")
root.geometry("1000x1400")
app = Main(root)
root.mainloop()