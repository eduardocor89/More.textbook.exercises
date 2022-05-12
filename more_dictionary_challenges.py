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



