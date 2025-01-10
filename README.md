# Probability of Winning on this Slot Machine

## Symbol Distribution:
There are 7 symbols on each reel:

- 🍒, 🍋, 🔔, ⭐, 7, BAR, 💎
- 🍒, 🍋, 🔔, ⭐, 7, BAR, 💎

The probability of landing any specific symbol on one reel is: 
P(symbol) = 1/7


## Recalculated Probabilities:

### 3 🍒:
The probability of 🍒 appearing on all 3 reels is:
P(3🍒) = (1/7)^3 = 1 / 343 ≈ 0.29%


### 2 🍒:
The probability of exactly 2 🍒 and one non-🍒 symbol:
P(2 🍒) = (3 choose 2) * (1 / 7)^2 * (6 / 7) = 3 * 1 / 49 * 6 / 7 = 18 / 343 ≈ 5.25%


### 1 🍒:
The probability of exactly 1 🍒 and two non-🍒 symbols:
P(1 🍒) = (3 choose 1) * (1 / 7)^1 * (6 / 7)^2 = 3 * 1 / 7 * 36 / 49 = 108 / 343 ≈ 31.49%


## Specific Matches in payout_table:

- **7, 7, 7:**  
P(7,7,7) = (1 / 7)^3 = 1 / 343 ≈ 0.29%

- **🔔, 🔔, 🔔:**  
P(🔔,🔔,🔔) = (1 / 7)^3 = 1 / 343 ≈ 0.29%


- **BAR, BAR, BAR:**  
P(BAR,BAR,BAR) = (1 / 7)^3 = 1 / 343 ≈ 0.29%


## Total Probability of Winning:
Adding up all the probabilities:
P(win) = P(3 🍒) + P(2 🍒) + P(1 🍒) + P(7,7,7) + P(🔔,🔔,🔔) + P(BAR,BAR,BAR) P(win) = 1 / 343 + 18 / 343 + 108 / 343 + 1 / 343 + 1 / 343 + 1 / 343 = 130 / 343 ≈ 37.91%


## Summary:
By adding the diamond symbol, the probability of winning decreases from **43.52%** to approximately **37.91%**. This is a more reasonable win probability for a slot machine, though still relatively high. Typical casino standards are around (~30% or less).

