# Divisible by ten
# Create a function named divisible_by_ten() that takes a list
# of numbers named "nums" as a parameter. Return the count of how 
# many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0:
      counter += 1
  return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))


# Greetings
# Create a function named add_greetings() which takes a list of 
# strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. 
# Add the string "Hello, " in front of each name in names and append the 
# greeting to the list. Return the new list containing the greetings. 

def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append("Hello, " + name)

  return greetings


print(add_greetings(["Owen", "Max", "Sophie"]))
print()

# Delete Starting Even Numbers
# Write a function called delete_starting_evens() that has a parameter
# named lst. The function should remove elements from the front of lst until
# the front of the list is not even. The function should then return lst.

# For example if lst started as [4,8,10,11,12,15] then calling the function
# should return [11,12,15]. 

# Make sure your function works even if every element in the list is even!

def delete_starting_evens(lst):
    i = 0
    while len(lst) >= 1 and lst[i] % 2 == 0:
      lst = lst[1:]
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# Odd indices
# Create a function named odd_indces() that has one parameter named lst.
# The function should create a new empty list and add every element from lst
# that has an odd index. The function should then return this new list. 

# For example, odd_indices([4,3,7,10,11,-2]) should return the list [3,10,-2]
print("\nOdd Indices")
def odd_indices(lst):
  new_lst = []
  for num in range(1, len(lst), 2):
    new_lst.append(lst[num])
  return new_lst


print(odd_indices([4, 3, 7, 10, 11, -2]))
# Take a moment to notice that a working solution iterates through the 
# range values. The key part of this loop iterates through a range of numbers
# that starts at one(and not zero), that's as long as the input list, and skips
# every other to yield the odd indices. 


# Exponents
# Create a function named exponents() that takes two lists as parameters 
# named bases and powers. Return a new list containing every number
# in bases raised to every number in powers. For example
# exponents([2,3,4],[1,2,3]) will yield [2,4,8,3,9,27,4,16,64]
print("\nExponents")
def exponents(bases, powers):
  answers = []
  for base in bases:
    for power in powers:
      answers.append(base**power)
  return answers

print(exponents([2, 3, 4], [1, 2, 3]))

