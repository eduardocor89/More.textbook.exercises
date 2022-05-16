"""
More dictionary challenges...
"""

# Word Length Dictionary
# Write a function named word_length_dictionary that takes a list of strings
# named words as a parameter and returns a dictionary of key/value paris where 
# every key is a word and every value is the length of that word

def word_length_dictionary(words):
  new_dictionary = {}
  for word in words:
    new_dictionary[word] = len(word)

  return new_dictionary
# Test
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


# Frequnecy Count
# Let's create a function named frequency_dictionary that takes a list of 
# elements named words as parameters and returns a dicitonary with the 
# frequency of each word

def frequency_dictionary(words):
  new_dictionary = {}
  for word in words:
    if word not in new_dictionary:
      new_dictionary[word] = 1
    else:
      new_dictionary[word] += 1
  return new_dictionary
# Test
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Count the first letter
# Let's create a function named count_first_letter that takes a dictionary named names and 
# returns a new dictionary where each key is the first name of the last name, and the value
# is the number of people whose last names begins with that letter. 

# Think of this names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# would return {"S" : 4, "L": 3}

def count_first_letter(names):
  letters = {}
  for key,value in names.items():
    if key[0] not in letters:
      letters[key[0]] = 0
    letters[key[0]] += len(value)
  return letters

# Test
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}


# Unique Values
# Let's create a funciton named unique_values that takes in a dictionary named my_dictionary and 
# returns the number of unique values in the dicitonary. 

def unique_values(my_dictionary):
  empty_list = []
  for value in my_dictionary.values():
    if value not in empty_list:
      empty_list.append(value)
  return len(empty_list)
# Test
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

