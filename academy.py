from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        business = 0
        compsci = 0
        science = 0
        engineering = 0
        theater = 0
        music = 0
        visual = 0
        culinary = 0
        med = 0

    def create_widgets(self):
        Label(self, text = "Answer the following questions to discover what BCA academy you belong in!").grid(row = 0, column = 1, columnspan = 2)

        Label(self, text="Pick an Animal:").grid(row=1, column=0, sticky=W)

        animals = ["snake", "owl", "mouse", "beaver", "parrot", "hummingbird", "peacock", "bee", "dolphin"]
        column = 1
        for word in animals:
            Radiobutton(self, text=word, variable=self.animal, value=word).grid(row=2, column=column, sticky=W)
            column += 1

        Label(self, text="Pick a Sport:").grid(row=3, column=0, sticky=W)

        sports = ["basketball", "ping-pong", "tennis", "baseball", "fencing", "golf", "volleyball", "track", "lacrosse"]
        column = 1
        for word in sports:
            Radiobutton(self, text=word, variable=self.sport, value=word).grid(row=2, column=column, sticky=W)
            column += 1

        sports = ["basketball", "ping-pong", "tennis", "baseball", "fencing", "golf", "volleyball", "track", "lacrosse"]
        column = 1
        for word in sports:
            Radiobutton(self, text=word, variable=self.sport, value=word).grid(row=3, column=column, sticky=W)
            column += 1

        places = ["museum", "arcade", "movies", "hiking", "club", "festival", "beach", "restaurant", "picnic"]
        column = 1
        for word in places:
            Radiobutton(self, text=word, variable=self.place, value=word).grid(row=4, column=column, sticky=W)
            column += 1

        Button(self, text="Click to See Your Story!", command=self.tell_story).grid(row=10, column=0, sticky=W)

        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=11, column=0, columnspan=4)

    def tell_story(self):
        animal = self.animal_ent.get()
        color = self.color_ent.get()
        noun = self.noun_ent.get()
        nouns = ""
        if self.is_salami.get():
            nouns += "salami, "
        if self.is_mayo.get():
            nouns += "mayo, "
        if self.is_egg.get():
            nouns += "egg, "
        adjectives = ""
        if self.is_bumpy.get():
            adjectives += "bumpy, "
        if self.is_stretchy.get():
            adjectives += "stretchy, "
        if self.is_wimpy.get():
            adjectives += "wimpy, "
        container = self.container.get()
        adjective = self.adjective.get()
        adjective2 = self.adjective2.get()

        story = "Make sure your lunch "
        story += container
        story += " is filled with nutritious, "
        story += adjective
        story += " food. Do not go to the "
        story += adjective2
        story += " food stand across the street from school. The hamburgers they serve are fried in "
        story += noun
        story += " and are made of "
        story += animal
        story += " meat. So take a sandwich made of cheese, "
        story += nouns
        story += "and tomatoes. It's much healthier! Drink "
        story += color
        story += " milk instead of nasty, "
        story += adjectives
        story += "and sugary sodas. "

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

root = Tk()
root.title("Rhianna's Mad Lib!")
app = Application(root)
root.mainloop()

