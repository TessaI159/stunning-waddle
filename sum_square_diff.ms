sum_of_squares = function(n)
  return floor((n * (n + 1) * ((2 * n) + 1)) / 6)
end function
  
square_of_sums = function(n)
  return floor(((n * (n + 1)) / 2) ^ 2)
end function

find_answer = function(n=100)
  return square_of_sums(n) - sum_of_squares(n)
end function

find_answer