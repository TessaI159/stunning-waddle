coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
solutions = [1] + [0] * target

def find_answer():
    for coin in coins:
        for i in range(coin, target + 1):
            solutions[i] += solutions[i - coin]
    return solutions[-1]
