from collections import defaultdict
import math


def change(coins: dict, value: int) -> dict:
    total = 0
    chosen_coins = {}
    coins = dict(sorted(coins.items(), key=lambda x: x[0], reverse=True))
    print(f"Coins: {coins}")
    for coin, n_coins in coins.items():
        for n in range(1, n_coins + 1):
            if total + coin > value:
                break
            else:
                total += coin
                if coin in chosen_coins:
                    chosen_coins[coin] += 1
                else:
                    chosen_coins.update({coin: n})

    print(total)
    print(chosen_coins)
    return chosen_coins


def change_dp(coins: dict, value: int) -> dict:
    """

    DP[i, s] = the minimum number of coins you need to reach s using coins 1..i,
        and inf if not possible

    BASE CASE:
    DP[0, s] = 0 if s = 0 else inf

    RECURSIVE STEP:
    DP[i, s] = min(1 + OPT[i-1, s-v_i], # provided v_i <= s
                    OPT[i-i, s])

    """
    n_coins = []
    for coin, amount in coins.items():
        for _ in range(amount):
            n_coins.append(coin)

    OPT = defaultdict()



# coins = {1: 3, 5: 0, 10: 3, 20: 1}
coins = {1: 3,  6: 5, 10: 3}

# change(coins, 42)
change_dp(coins, 42)
