import tkinter as tk
import random

guessed_letters = set()  # Add this at the top, outside the function
m=1 

def GOT():
    global m
    guess = entry.get().strip().lower()
    entry.delete(0, tk.END)
    if not guess or len(guess) != 1 or not guess.isalpha():
        label.config(text="Enter a single letter.")
        return

    if guess not in word.lower():
        if m == 1:
            canvas.create_oval(200, 50, 260, 110, outline="white", width=5)#head
        elif m == 2:
            canvas.create_line(230, 110, 230, 170, width=5, fill="white",)#body
        elif m == 3:
            canvas.create_line(230, 120, 190, 150, width=5, fill="white")#left arm
        elif m == 4:
            canvas.create_line(230, 120, 270, 150, width=5, fill="white")#right arm
        elif m == 5:
            canvas.create_line(230, 170, 190, 200, width=5, fill="white")#left leg
        elif m == 6:
            canvas.create_line(230, 170, 270, 200, width=5, fill="white")#right leg
        elif m ==7:
            label.config(text=f"GAME OVER!!! The word was: {word.upper()}")
            label.place(x=30, y=100)
            entry.config(state="disabled")
            button.config(state="disabled")
        m += 1

 

    guessed_letters.add(guess)
    display = ""
    for char in word.lower():
        if char in guessed_letters:
            display += char + " "
        else:
            display += "_ "
    label.config(text=display)

    if "_" not in display.replace(" ", ""):
        label.config(text=f"CONGRATS!!! You guessed it right: {word.upper()}")
        label.place(x=30, y=100)
        entry.config(state="disabled")
        button.config(state="disabled")

root = tk.Tk()
root.title("Doing Timepass")
root.geometry("700x700")

Words = ["Home", "Game", "Science", "Maths", "Geography", "Politics", "Cricket", "Football", "Movies", "Music", "Books", "Art", "History", "Nature", "Technology", "Space", "Ocean", "Animals", "Plants", "Weather", "Health", "Fitness", "Travel", "Food", "Cooking", "Fashion", "Photography", "Education", "Economics",]
word = random.choice(Words)

label = tk.Label(root, text="Guess the Word Game", font=("Arial", 24))
label.place(x=160, y=100)

entry = tk.Entry(root, width=35, font=("Arial", 18))
entry.place(x=120, y=200)

button = tk.Button(root, text="Submit", font=("Arial", 18), command=GOT)
button.place(x=300, y=250)

canvas = tk.Canvas(root, width=500, height=300, bg="Black")
canvas.place(x=100, y=320)

canvas.create_line(100, 250, 100, 50, width=5, fill="white")
canvas.create_line(100, 50, 250, 50, width=5, fill="white")

root.mainloop()