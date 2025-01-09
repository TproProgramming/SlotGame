import tkinter as tk
from tkinter import messagebox
import random

def spin_reels():
    """Spin the slot machine reels and update the GUI."""
    global balance, last_win
    if bet_size.get() > balance:
        messagebox.showerror("Error", "Bet exceeds available balance!")
        return

    symbols = ["🍒", "🍋", "🔔", "⭐", "7", "BAR", "💎"]
    reels = [random.choice(symbols) for _ in range(3)]

    # Update the reels display
    reel_1.config(text=reels[0])
    reel_2.config(text=reels[1])
    reel_3.config(text=reels[2])

    # Calculate the payout
    payout = calculate_payout(reels, bet_size.get())
    last_win = payout
    if payout > 0:
        result_label.config(text=f"You win ${payout}!", fg="green")
        balance += payout
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
        ("💎", "💎", "💎"): 75,
        ("🔔", "🔔", "🔔"): 50,
        ("BAR", "BAR", "BAR"): 25,
    }
    if reels.count("🍒") == 3:
        return 100 * bet
    elif reels.count("🍒") == 2:
        return 2 * bet
    elif reels.count("🍒") == 1:
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

# Initialize the game
balance = 100
last_win = 0

# Create the main window
root = tk.Tk()
root.title("Slot Machine")
root.geometry("500x500")
root.config(bg="black")

# Static background
background = tk.Label(root, bg="darkblue")
background.place(relwidth=1, relheight=1)

# Display Labels
balance_label = tk.Label(root, text=f"Balance: ${balance}", font=("Arial", 14), fg="white", bg="darkblue")
balance_label.pack(pady=10)

last_win_label = tk.Label(root, text=f"Last Win: ${last_win}", font=("Arial", 14), fg="white", bg="darkblue")
last_win_label.pack(pady=10)

bet_size = tk.IntVar(value=1)
bet_label = tk.Label(root, text="Bet Size:", font=("Arial", 14), fg="white", bg="darkblue")
bet_label.pack(pady=5)
bet_value_label = tk.Label(root, textvariable=bet_size, font=("Arial", 14), fg="white", bg="darkblue")
bet_value_label.pack(pady=5)

# Reels Display
reel_frame = tk.Frame(root, bg="darkblue")
reel_frame.pack(pady=20)

reel_1 = tk.Label(reel_frame, text="🍒", font=("Arial", 30), fg="white", bg="darkblue")
reel_1.pack(side="left", padx=10)

reel_2 = tk.Label(reel_frame, text="🍋", font=("Arial", 30), fg="white", bg="darkblue")
reel_2.pack(side="left", padx=10)

reel_3 = tk.Label(reel_frame, text="🔔", font=("Arial", 30), fg="white", bg="darkblue")
reel_3.pack(side="left", padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="darkblue")
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
