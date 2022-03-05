
# Create a list called single_digits that consists of the numbers 0-9
single_digits = [i for i in range(0,10)]
print(single_digits)

# Create a for loop that goes through single_digits and prints out each one
single_digits = [0,1,2,3,4,5,6,7,8,9]
for i in single_digits:
  print(i)

# Before the loop, create a list called squares. Assign it to be an empty list to begin with
squares = []

# Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element
for i in single_digits:
  squares.append(i**2)
print(squares)

# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power. 
cubes = [i**3 for i in single_digits]
print(cubes)
