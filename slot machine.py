import random

def spin_row():
    symbols = ["🍒", "🍋", "🍉", "⭐", "🔔"]
    results = []
    for _ in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row.count(row[0]) == 3:
        return bet * 5   # jackpot
    elif row.count(row[0]) == 2 or row.count(row[1]) == 2:
        return bet * 2   # two same
    else:
        return 0

def main():
    balance = 100
    print("******************************")
    print("Welcome to the python Slot ")
    print("symbols: 🍒 🍋 🍉 ⭐ 🔔 ")
    print("******************************")

    while balance > 0:
        print(f"Current Balance: BDT {balance}")
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid number. Please enter valid number.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient Funds.")
            continue
        if bet <= 0:
            print("Bet must be greater than Zero.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        if payout > 0:
            print(f"🎉 You won {payout} BDT!")
        else:
            print(" No win this time.")

    print("\nThanks for playing! Goodbye 👋")

if __name__ == "__main__":
    main()
