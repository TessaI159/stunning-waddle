coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
solutions = [1] + [0] * target

findAnswer = function()
  for coin in coins
    for i in range(coin, target)
      solutions[i] = solutions[i] + solutions[i - coin]
    end for
  end for
  return solutions[-1]
end function