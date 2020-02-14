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

root = Tk()
root.title("Main screen")
root.geometry("1000x1400")
app = Main(root)
root.mainloop()