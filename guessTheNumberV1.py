import tkinter as tk
from tkinter import ttk
import random

def check_guess():
    try:
        guess = int(guess_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        return

    random_number = random.randint(1, 10)

    if guess == random_number:
        result = "You won!"
    else:
        result = f"""The correct number was {random_number}.
    The game is over Give up on your dreams and 死ぬ!
                Just Kidding! Try again!😃"""

    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Use ttk style and choose a modern theme
style = ttk.Style(root)
# List available themes with: style.theme_names()
style.theme_use('clam')

# Create a frame with padding for better layout management
frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

# Instruction label with custom font and padding
instruction_label = ttk.Label(frame, text="Enter a number between 1 and 10:", font=("Helvetica", 14))
instruction_label.pack(pady=10)

# Entry widget for the guess with styling
guess_entry = ttk.Entry(frame, font=("Helvetica", 14))
guess_entry.pack(pady=10)

# Button to check the guess
check_button = ttk.Button(frame, text="Check Guess", command=check_guess)
check_button.pack(pady=10)

# Label to display the result
result_label = ttk.Label(frame, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
