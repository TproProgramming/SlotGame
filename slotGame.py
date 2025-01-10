import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame 

def spin_reels():
    """Spin the slot machine reels and update the GUI."""
    global balance, last_win
    if bet_size.get() > balance:
        messagebox.showerror("Error", "Bet exceeds available balance!")
        return

    symbols = ["cherries", "horseshoe", "bell", "clover", "7", "bar", "diamond"]
    reels = [random.choice(symbols) for _ in range(3)]

    # Update the reels display with images
    reel_1.config(image=images[reels[0]])
    reel_2.config(image=images[reels[1]])
    reel_3.config(image=images[reels[2]])

    # Calculate the payout
    payout = calculate_payout(reels, bet_size.get())
    last_win = payout
    if payout > 0:
        result_label.config(text=f"You win ${payout}!", fg="green")
        balance += payout
        win_sound.play()
        if payout > 49:
            jackpot_sound.play(2)
    else:
        result_label.config(text="No win, better luck next time!", fg="red")
        balance -= bet_size.get()

    # Update balance and last win display
    balance_label.config(text=f"Balance: ${balance}")
    last_win_label.config(text=f"Last Win: ${last_win}")

    if balance <= 0:
        messagebox.showinfo("Game Over", "You're out of money!")
        root.quit()

def calculate_payout(reels, bet):
    """Calculate the payout based on the reels and bet."""
    payout_table = {
        ("7", "7", "7"): 1000,
        ("diamond", "diamond", "diamond"): 500,
        ("clover", "clover", "clover"): 100,
        ("bell", "bell", "bell"): 50,
        ("horseshoe", "horseshoe", "horseshoe"): 50,
        ("bar", "bar", "bar"): 25,
    }
    if reels.count("cherries") == 3:
        return 50 * bet
    elif reels.count("cherries") == 2:
        return 2 * bet
    elif reels.count("cherries") == 1:
        return 1 * bet
    elif tuple(reels) in payout_table:
        return payout_table[tuple(reels)] * bet
    return 0

def increase_bet():
    """Increase the bet size."""
    if bet_size.get() < balance:
        bet_size.set(bet_size.get() + 1)

def decrease_bet():
    """Decrease the bet size."""
    if bet_size.get() > 1:
        bet_size.set(bet_size.get() - 1)
        
# Initialize pygame mixer for music
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load("sound/bgMusic.wav")
pygame.mixer.music.set_volume(0.5)  # Adjust the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Loop indefinitely

# Load win sound
win_sound = pygame.mixer.Sound("sound/smallWin.wav")
win_sound.set_volume(1)  # Adjust the volume for the win sound

#Load jackpot win sound
jackpot_sound = pygame.mixer.Sound("sound/jackpotSound.wav")
jackpot_sound.set_volume(1)

# Initialize the game
balance = 100
last_win = 0

# Create the main window
root = tk.Tk()
root.title("Slot Machine")
root.geometry("500x500")
root.config(bg="darkblue")

# Load images
image_files = {
    "cherries": "images/cherries.png",
    "horseshoe": "images/horseshoe.png",
    "bell": "images/bell.png",
    "clover": "images/clover.png",
    "7": "images/7.png",
    "bar": "images/bar.png",
    "diamond": "images/diamond.png",
}
images = {name: ImageTk.PhotoImage(Image.open(path).resize((100, 100))) for name, path in image_files.items()}

# Display Labels
balance_label = tk.Label(root, text=f"Balance: ${balance}", font=("Arial", 14), fg="yellow", bg="darkblue")
balance_label.pack(pady=10)

last_win_label = tk.Label(root, text=f"Last Win: ${last_win}", font=("Arial", 14), fg="yellow", bg="darkblue")
last_win_label.pack(pady=10)

bet_size = tk.IntVar(value=1)
bet_label = tk.Label(root, text="Bet Size:", font=("Arial", 14), fg="yellow", bg="darkblue")
bet_label.pack(pady=5)
bet_value_label = tk.Label(root, textvariable=bet_size, font=("Arial", 14), fg="yellow", bg="darkblue")
bet_value_label.pack(pady=5)

# Reels Display
reel_frame = tk.Frame(root, bg="darkblue")
reel_frame.pack(pady=20)

reel_1 = tk.Label(reel_frame, image=images["cherries"], bg="darkblue")
reel_1.pack(side="left", padx=10)

reel_2 = tk.Label(reel_frame, image=images["clover"], bg="darkblue")
reel_2.pack(side="left", padx=10)

reel_3 = tk.Label(reel_frame, image=images["bell"], bg="darkblue")
reel_3.pack(side="left", padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="yellow", bg="darkblue")
result_label.pack(pady=10)

# Control Buttons
control_frame = tk.Frame(root, bg="darkblue")
control_frame.pack(pady=20)

increase_bet_button = tk.Button(control_frame, text="+", command=increase_bet, font=("Arial", 14), fg="white", bg="green")
increase_bet_button.pack(side="left", padx=10)

spin_button = tk.Button(control_frame, text="Spin", command=spin_reels, font=("Arial", 14), fg="white", bg="red")
spin_button.pack(side="left", padx=10)

decrease_bet_button = tk.Button(control_frame, text="-", command=decrease_bet, font=("Arial", 14), fg="white", bg="green")
decrease_bet_button.pack(side="left", padx=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 14), fg="white", bg="darkred")
exit_button.pack(pady=20)

# Run the main loop
root.mainloop()
