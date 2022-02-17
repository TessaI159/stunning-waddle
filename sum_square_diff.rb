def sum_of_squares(n)
  (n * (n + 1) * ((2 * n) + 1)) / 6
end

def square_of_sums(n)
  ((n * (n + 1)) / 2) ** 2
end

def find_answer(n=100)
  (square_of_sums n) - (sum_of_squares n)
end

find_answer
