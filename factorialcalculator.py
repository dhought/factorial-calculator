n = int(input("Choose a number: "))

# This function takes the user input and uses recursion to calculate the factorial of the number
def factorial(n):
  x = 1
  fact = n * (n - x)
  while (n - x) > 1:
    x += 1
    fact = fact * (n - x)
  print(str(n) + "! =" , fact)


factorial(n)
