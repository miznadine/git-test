import sys

dollars = 1
quarters = 1
dimes = 1
nickels = 1
pennies = 1

def change(do, qu, di, ni, pe):
    total = (1 * do) + (0.25 * qu) + (0.1 * di) + (0.05 * ni) + (0.01 * pe)
    print(f"The total value of your change is ${total:.2f}")
    
change(dollars, quarters, dimes, nickels, pennies)