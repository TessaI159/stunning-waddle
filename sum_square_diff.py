def sum_of_squares(n):
    return (n * (n + 1) * ((2 * n) + 1)) // 6

def square_of_sums(n):
    return int(((n * (n + 1)) / 2) ** 2)

def find_answer(n=100):
    return square_of_sums(n) - sum_of_squares(n)


find_answer()
