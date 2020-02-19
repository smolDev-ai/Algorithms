#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # find the minimum buy price and maximum sell price and determine profit
    # subtract min from max return.
    
    # keep track of values
    minimum = min(prices[0], prices[1])
    profit = prices[1] - prices[0]

    # if prices is greater than two items
    if len(prices) > 2:
        # starting at the third index because we're storing the first and second indices in minimum
        for i in range(2, len(prices)):
            # if current index minus minimum is greater than profit set profit to that value
            if prices[i] - minimum > profit:
                profit = prices[i] - minimum
            # if current index is less than minimum set the minimum to that value
            if prices[i] < minimum:
                minimum = prices[i]
    return profit




if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))