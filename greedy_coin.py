#!/usr/bin/env python
""" Greedy Coin Change Algorithm
1. The function greedy_coin takes one argument, the amount of change to be given to the customer.
2. The function prints a statement to tell the customer how much change they are getting.
3. The function initializes a list of coins (quarters, dimes, nickels, and pennies) and a dictionary that maps the coins to their denominations.
4. The function initializes a dictionary that will hold the number of coins of each type.
5. The function goes through the list of coins and initializes the dictionary with a value of 0 for each coin.
6. The function goes through the list of coins.
7. The function subtracts the coin from the amount of change the customer is getting until the amount of change is less than the coin.
8. The function then increments the number of coins of that type by 1.
9. The function prints the number of each coin type the customer is getting.
10. The function returns the dictionary with the number of each coin type. 
"""

import click


def greedy_coin(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""

    print(f"Your change for {change}: ")
    remaining_cents = int(round(change * 100))
    coins = [(0.25, 25), (0.10, 10), (0.05, 5), (0.01, 1)]
    coin_lookup = {0.25: "quarter", 0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    for coin, _ in coins:
        coin_dict[coin] = 0
    for coin, cents in coins:
        coin_dict[coin], remaining_cents = divmod(remaining_cents, cents)
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


@click.command()
@click.argument("change", type=float)
def main(change):
    """Return the minimum number of coins for a given change

    Example: ./greedy_coin.py 0.99
    """
    greedy_coin(change)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
