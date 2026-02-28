"""
Scenario 1 — Money / Coins

Problem: Given a total amount of money in rupees, find out how many notes and coins of each denomination you need.

Example:

Input: 1237 rupees

Output: 1000*1 note, 200*1 note, 20*1 note, 10*1 coin, 5*1 coin, 2*1 coin

Why it's like the time example:

Just like you divide seconds by 3600 to get hours, here you divide money by the biggest note to get how many notes, 
then repeat for smaller denominations.
"""

# Function to convert total money into notes and coins
def split_money(amount):
    # Step 1: 1000Rs notes
    notes_1000 = amount // 1000
    remaining_amount = amount - notes_1000 * 1000

    # Step 2: 200Rs notes
    notes_200 = remaining_amount // 200
    remaining_amount = remaining_amount - notes_200 * 200

    # Step 3: 100Rs notes
    notes_100 = remaining_amount // 100
    remaining_amount = remaining_amount - notes_100 * 100

    # Step 4: 50Rs notes
    notes_50 = remaining_amount // 50
    remaining_amount = remaining_amount - notes_50 * 50

    # Step 5: 20Rs notes
    notes_20 = remaining_amount // 20
    remaining_amount = remaining_amount - notes_20 * 20

    # Step 6: 10Rs coins
    coins_10 = remaining_amount // 10
    remaining_amount = remaining_amount - coins_10 * 10

    # Step 7: 5Rs coins
    coins_5 = remaining_amount // 5
    remaining_amount = remaining_amount - coins_5 * 5

    # Step 8: 2Rs coins
    coins_2 = remaining_amount // 2
    remaining_amount = remaining_amount - coins_2 * 2

    # Step 9: 1Rs coins
    coins_1 = remaining_amount  # remaining money is all 1Rs coins

    # Return all counts as a tuple (tuple unpacking can be used)
    return (notes_1000, notes_200, notes_100, notes_50, notes_20,
            coins_10, coins_5, coins_2, coins_1)


# Scenario: We have a total amount of 1237 rupees
# Using tuple unpacking to store each denomination separately
notes_1000, notes_200, notes_100, notes_50, notes_20, coins_10, coins_5, coins_2, coins_1 = split_money(1237)

# Display the result in a readable way
print("Breakdown of 1237 rupees into notes and coins:")
print(f"1000Rs notes: {notes_1000}")
print(f"200Rs notes: {notes_200}")
print(f"100Rs notes: {notes_100}")
print(f"50Rs notes: {notes_50}")
print(f"20Rs notes: {notes_20}")
print(f"10Rs coins: {coins_10}")
print(f"5Rs coins: {coins_5}")
print(f"2Rs coins: {coins_2}")
print(f"1Rs coins: {coins_1}")