from tkinter import *  # Import all tkinter classes
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'arial'


french_english = pd.read_csv('./data/french_words.csv')
to_learn = french_english.to_dict(orient='records') # orient changes the way that the dictionary is created.

def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])

word = random.choice(to_learn)['French']

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # This makes the image containing the Canvas 50 x 50 larger.

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text='', font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()

