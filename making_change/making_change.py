#!/usr/bin/python

import sys

def making_change(amount, denominations):
    # Take in an amount in pennies and return that amount in coins?
    # would rather do this in an iterative fashion than recursive since I'm still struggling to 
    # understand recursion.

    # list comprehension for the cache to create a list full of zeros that matches the length of amount + 1
    cache = [0 for i in range(0, amount+1)]
    # the first element in the list should be 1
    cache[0] = 1

    for coins in denominations:
        for higher_amount in range(coins, amount + 1):
            # setting the cache's current index to be the sum of itself minus 
            # whatever coin amount it's on.
            cache[higher_amount] = cache[higher_amount] + cache[higher_amount-coins]
    return cache[amount]


print(making_change(100, [1, 5, 10, 25, 50]))




if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")