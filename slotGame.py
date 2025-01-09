import random

def spin_reels():
    """Spin the slot machine reels and return the result."""
    symbols = ["🍒", "🍋", "🔔", "⭐", "7", "BAR"]
    return [random.choice(symbols) for _ in range(3)]

def calculate_payout(reels, bet):
    """Calculate the payout based on the reels and bet."""
    payout_table = {
        ("🍒", "🍒", "🍒"): 100,
        ("7", "7", "7"): 1000,
        ("🔔", "🔔", "🔔"): 50,
        ("BAR", "BAR", "BAR"): 25,
    }
    
    # Check for three cherries
    if reels.count("🍒") == 3:
        return 100 * bet
    # Check for two cherries
    elif reels.count("🍒") == 2:
        return 10 * bet
    # Check for one cherry
    elif reels.count("🍒") == 1:
        return 1 * bet
    # Check for exact match in the payout table
    elif tuple(reels) in payout_table:
        return payout_table[tuple(reels)] * bet
    
    return 0


def display_reels(reels):
    """Display the reels."""
    print("|".join(reels))

def main():
    """Main game loop."""
    print("Welcome to the Classic Slot Machine!")
    print("Match symbols on the payline to win.")
    print("Payout Table:")
    print("3 🍒 = 100x, 3 7 = 50x, 3 🔔 = 20x, 3 BAR = 15x, 2 🍒 = 10x, 1 🍒 = 1x")

    balance = 100  # Starting balance
    maxBet = 500 
    while balance > 0:
        print(f"\nCurrent balance: ${balance}")
        try:
            bet = int(input("Enter your bet amount: "))
            if bet <= 0 or bet > balance or bet > maxBet:
                print("Invalid bet amount. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        print("Spinning reels...")
        reels = spin_reels()
        display_reels(reels)

        payout = calculate_payout(reels, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
            balance += payout
        else:
            print("No win this time. Better luck next spin!")
            balance -= bet

        if balance <= 0:
            print("Game over! You ran out of money.")
            break


if __name__ == "__main__":
    main()
