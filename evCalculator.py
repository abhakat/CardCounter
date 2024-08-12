import matplotlib.pyplot as plt
import numpy as np

# Define the bet spread and house edge
bet_spread = {
    -2: 10,   # Bet $10 at TC -2
    -1: 10,   # Bet $10 at TC -1
    0: 10,    # Bet $10 at TC 0
    1: 20,    # Bet $20 at TC +1
    2: 30,    # Bet $30 at TC +2
    3: 50,    # Bet $50 at TC +3
    4: 100,   # Bet $100 at TC +4
    5: 200    # Bet $200 at TC +5
}

house_edge_by_decks = {
    1: 0.0017,  # Single deck, optimal rules (0.17%)
    2: 0.0035,  # Two decks (0.35%)
    4: 0.0048,  # Four decks (0.48%)
    6: 0.0050,  # Six decks (0.50%)
    8: 0.0055   # Eight decks (0.55%)
}

house_edge = 0.005
true_count_range = (-2, 5)

# Calculate player advantage at each True Count
true_count_to_advantage = {
    tc: (tc * 0.005 - house_edge) for tc in range(true_count_range[0], true_count_range[1] + 1)
}

# Calculate expected value for each True Count
ev = {tc: bet_spread.get(tc, 0) * true_count_to_advantage[tc] for tc in true_count_to_advantage}

# Assume each True Count occurs with equal probability and simulate over time
time = np.arange(1, 1001)
cumulative_profit = np.cumsum([np.random.choice(list(ev.values())) for _ in time])

# Plotting the theoretical profit over time
plt.figure(figsize=(10, 6))
plt.plot(time, cumulative_profit, label="Theoretical Profit")
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.title("Theoretical Profit Over Time with Bet Spread")
plt.xlabel("Time (Number of Hands)")
plt.ylabel("Cumulative Profit ($)")
plt.legend()
plt.grid(True)
plt.show()
