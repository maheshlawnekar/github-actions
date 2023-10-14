
def sum(numbers):
  """Returns the sum of the numbers in the given list """

  total = 0
  for number in numbers:
    total += number
  return total

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    sum_ = sum(numbers)
    print(sum_)
