"""
In here I practice with dictionaries. 
"""

# Sum Values
# Write a function named sum_values that takes a dictionary 'my_dictionary'
# as a parameter. The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total
# Test
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


# Even Keys
# Let us make a function called sum_even_keys that takes a dictionary
# named my_dictionary with all integer keys and values, as a parameter.
# This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
  total = 0
  for key,value in my_dictionary.items():
    if key % 2 == 0:
      total += value

  return total
# Test
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


# Add Ten
# Create a function named add_ten that takes a dictionary with integer values 
# named my_dictionary as a parameter. The function should add 10 to every value
# in my_dictionary and return my_dictionary

# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  
  return my_dictionary

# Test
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Values that are keys
# Let's make a function named values_that_are_keys() that takes a dictionary
# named my_dictionary as a parameter and that returns a list of all values in the
# the dictionary that are ALSO keys.

def values_that_are_keys(my_dictionary):
  values = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      values.append(value)
  return values
# Test
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]



# Largest Value
# Let's write a spin off of the max() function named max_key() that takes a dictionary as a parameter.
# The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):
  max_key = 0
  max_value = float("-inf")
  for key,value in my_dictionary.items():
    if value > max_value:
      max_key = key
      max_value = value
  return max_key
# Test
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
