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
        Label(self, text = "WELCOME TO L-CARM!", font= "Helvetica 30"
                                                        ).grid(row = 0, columnspan = 8)
        Label(self, text = "Basic Applications", font = "Helvetica 20"
              ).grid(row = 1, columnspan = 1)
        Label(self, text = "Quizzes", font = "Helvetica 20"
              ).grid(row = 5, columnspan = 1)
        Label(self, text = "").grid(row = 4, columnspan = 3)

        Button(self, text = "Academy", font = "Helvetica 10", command = self.academy
               ).grid(row = 6, column = 0)
        Button(self, text = "Aesthetic", font = "Helvetica 10", command = self.aesthetic
               ).grid(row = 6, column = 2, sticky = W)
        Button(self, text = "Color person", font = "Helvetica 10", command = self.color_person
               ).grid(row = 6, column = 4)
        Button(self, text = "Disney Princesses", font = "Helvetica 10", command = self.disney_princess
               ).grid(row = 6, column = 6)
        Button(self, text = "Hogwarts House", font = "Helvetica 10", command = self.hogwarts_house
               ).grid(row = 6, column = 8)
        Button(self, text = "Spirit Animal", font = "Helvetica 10", command = self.spirit_animal
               ).grid(row = 6, column = 10)
        Button(self, text = "Third Grade Quiz", font = "Helvetica 10", command = self.third_grade_quiz
               ).grid(row = 6, column = 12)
        Button(self, text = "Zodiac Sign", font = "Helvetica 10", command = self.zodiac_sign
               ).grid(row = 6, column = 14)
root = Tk()
root.title("Main screen")
root.geometry("1000x1400")
app = Main(root)
root.mainloop()