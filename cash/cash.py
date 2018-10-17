from cs50 import get_float

while True:
    f = get_float("Change owed: ")
    if (f >= 0):
        break
# converts to cents.
balance = round(f * 100)
print("Multiplied by 100: ", balance)
g = 0

# check for quarters
q = 25
coins = 0
if (balance >= q):
    g = balance//q
    print("No of Quarters: ", g)
    coins = coins + g
    print("Coins used: ", coins)
    balance = balance % q  # use modulus to find the balance
    print("remaining balance: ", balance)

# check for dimes
d = 10
if (balance >= d):
    g = balance // d
    print("No of dimes: ", g)
    coins = coins + g
    print("Coins used: ", coins)
    balance = balance % d  # use modulus to find the balance
    print("remaining balance:  ", balance)
# check for nickel
n = 5
if (balance >= n):
    g = balance // n
    print("No of nickel:  ", g)
    coins = coins + g
    print("Coins used:  ", coins)
    balance = balance % n  # use modulus to find out the balance
    print("rem: ", balance)

# check for pennies
coins = coins + balance
print("No of pennies: ", balance)
print("Total coins used: ", coins)
print(coins)
