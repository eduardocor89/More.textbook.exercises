'''
String methods exercises. Some maybe more interesting than others
'''

# Count Letters:
# Write a function called unique_english_letters that takes the string
# word as a parameter. The function should return the total number of unique 
# letters in the string. Uppercase and lowercase should be counded as different letters

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  unique_letters = []
  for letter in word:
    if letter not in unique_letters:
      unique_letters.append(letter)
  return len(unique_letters)

# Test
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("Eddie"))
# Should print 4

## Note: I could've just as easily created a counter for the number of unique letters
## and return that, but in case someone wanted to know what those letters were, the counter
## wouldn't have been able to provide that answer. By putting them in a list, I can both return
## the number of them, but also what they were if I needed that information


# Count X:
# Let's write a function named count_char_x that takes a string named word and a single character
# named x as parameters. The function should return the number of times x appeared in word

def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter == x:
      count += 1
  return count

# Test
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
print(count_char_x("Eddie","E"))
# should print 1


# Count Multi X 
# Let's write a function named count_multi_char_x that takes a string named word and a string
# named x. This funciton should do the same thing as the count_char_x function- it should return the 
# number of times x appears in word. This time, however, make sure your function works with strings
# with multiple characters. For example: "mississipi" has 2 occurrences of iss. 

def count_multi_char_x(word, x):
  result = word.split(x)
  print(result)
  return len(result)-1

# Test
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

'''
This one was particularly tricky because I had to think outside of the characters themselves
and think about the problem from a bird's eye view. In this case, I sectioned the string into chunks
and counted how many chunks were removed
'''


# Substring between
# Let's write a function named substring_between_letters that takes a string named word
# a single character named start and another character named end. This function should return
# the substring between the first occurrence of start and end in word. For example:
# substring_between_letters("apple", "p","e") should return "pl"

def substring_between_letters(word,start,end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index == -1 or end_index == -1:
    return word
  else:
    return word[start_index + 1 :end_index]

# Test
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# X length
# Let's create a function called x_length_words that takes a string named sentence
# and an integer named x as parameters. This function should return True if every word
# in sentence has a length greater than or equal to x

def x_length_words(sentence, x):
  split_sentence = sentence.split(' ')
  for word in split_sentence:
    if len(word) >= x:
      return True
    else:
      return False

# Test
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
