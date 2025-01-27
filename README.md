# Slot Machine Game

A simple slot machine simulation built using Python's `tkinter` library for the GUI and `pygame` for background music and sound effects.

## Features
- Spin the reels and try your luck to win!
- Dynamic payout calculation based on reel results.
- Adjustable bet size.
- Background music and sound effects for wins and jackpots.
- Graphical user interface with reel images and real-time balance updates.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `tkinter` (usually included with Python)
  - `Pillow` (for image handling)
  - `pygame` (for music and sound effects)

To install the necessary libraries, run:
```bash
pip install pillow pygame
```

### File Structure
Ensure the following directory structure:
```
project_directory/
|-- images/
|   |-- cherries.png
|   |-- horseshoe.png
|   |-- bell.png
|   |-- clover.png
|   |-- 7.png
|   |-- bar.png
|   |-- diamond.png
|-- sound/
|   |-- bgMusic.wav
|   |-- smallWin.wav
|   |-- jackpotSound.wav
|-- slot_machine.py
```

Place all the corresponding images and sound files in the `images` and `sound` folders, respectively.

## Usage
1. Navigate to the project directory:
   ```bash
   cd project_directory
   ```
2. Run the script:
   ```bash
   python slot_machine.py
   ```
3. Use the buttons to adjust the bet size, spin the reels, and try your luck!

## Gameplay
- **Balance**: Starts with $100.
- **Bet Size**: Adjustable using the `+` and `-` buttons.
- **Spin**: Click the `Spin` button to play.
- **Win Conditions**: The payout depends on the combination of symbols displayed on the reels. Special payouts for matching symbols and cherries.
- **Game Over**: The game ends when your balance reaches $0.

## Payout Table
| Combination                       | Payout Multiplier |
|-----------------------------------|-------------------|
| 7 - 7 - 7                         | 1000x             |
| Diamond - Diamond - Diamond       | 500x              |
| Clover - Clover - Clover          | 100x              |
| Bell - Bell - Bell                | 50x               |
| Horseshoe - Horseshoe - Horseshoe | 50x               |
| Bar - Bar - Bar                   | 25x               |
| 3 Cherries                        | 50x               |
| 2 Cherries                        | 2x                |
| 1 Cherry                          | 1x                |

## Sound Effects
- Background music plays continuously.
- **Win sound**: Plays when you win a small amount.
- **Jackpot sound**: Plays for big wins.

## Customization
You can customize the following:
- **Starting Balance**: Modify the `balance` variable.
- **Payout Rules**: Edit the `payout_table` dictionary and cherry-specific conditions in the `calculate_payout` function.
- **Images and Sounds**: Replace the files in the `images` and `sound` folders with your own.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments
- [Pillow](https://python-pillow.org/) for image handling.
- [Pygame](https://www.pygame.org/) for sound and music integration.

