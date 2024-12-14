import tkinter as tk
from tkinter import messagebox
import random

# Main game logic
def play_round(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        global user_score
        user_score += 1
    else:
        result = "You lose!"
        global computer_score
        computer_score += 1

    result_label.config(text=result)
    update_scores()

# Update the scores
def update_scores():
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

# Reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
    user_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")
    result_label.config(text="")

# Exit the game
def exit_game():
    root.destroy()

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x300")

# Create labels and buttons
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16)).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", font=("Arial", 14), command=lambda: play_round("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", font=("Arial", 14), command=lambda: play_round("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", font=("Arial", 14), command=lambda: play_round("Scissors")).grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="You chose: ", font=("Arial", 14))
user_label.pack(pady=5)
computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 14))
computer_label.pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)
score_label = tk.Label(root, text="User: 0  Computer: 0", font=("Arial", 14))
score_label.pack(pady=10)

tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game).pack(side=tk.LEFT, padx=10, pady=20)
tk.Button(root, text="Exit", font=("Arial", 14), command=exit_game).pack(side=tk.RIGHT, padx=10, pady=20)

# Run the main loop
root.mainloop()
