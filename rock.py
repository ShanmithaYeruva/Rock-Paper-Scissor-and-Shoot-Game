import random
import tkinter as tk
import pygame

all_results = []
results = []

draw = "It's a draw!"
win = "You win. Horray!"
loss = "You lose. Only luck. Don't give up hope."

def round_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return draw
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return win
    else:
        return loss

def on_player_choice(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = round_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose {player_choice}\nComputer chose {computer_choice}\n{result}")

def show_results():
    result_window = tk.Toplevel(root)
    result_window.title("Game Results")
    result_text = "\n".join(results) if results else "No results yet!"
    result_label = tk.Label(result_window, text=result_text, justify="left", font=("Arial", 10))
    result_label.pack(padx=10, pady=10)

root = tk.Tk()
root.title("Rock, Paper, Scissors, Shoot!")

print("Welcome")
print("Do you know the rules of the game?")

title_label = tk.Label(root, text="Rock, Paper, Scissors, Shoot!", font=("Arial", 16))
title_label.pack()

# Result label
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12))
result_label.pack()

# Buttons for player choices
rock_button = tk.Button(root, text="Rock", command=lambda: on_player_choice("Rock"), width=15)
paper_button = tk.Button(root, text="Paper", command=lambda: on_player_choice("Paper"), width=15)
scissors_button = tk.Button(root, text="Scissors", command=lambda: on_player_choice("Scissors"), width=15)

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

# Button to show saved results
results_button = tk.Button(root, text="Show Results", command=show_results, width=15)
results_button.pack(pady=10)

# Run the application
root.mainloop()