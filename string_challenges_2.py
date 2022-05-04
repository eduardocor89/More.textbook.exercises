"""
More exercises on string methods. 
"""

# Check Name
# Let's write a function called check_for_name that takes two strings as parameters
# named sentence and name and returns True if name appears in sentence. Return False
# otherwise. 

def check_for_name(string,name):
  if name.lower() in string.lower():
    return True
  return False
# Test
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# I realize I could've also written it like so:
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()


# Every Other Letter
# Let's write a function called every_other_letter that takes a string named word
# as a parameter and returns a string containing every other letter in word.

def every_other_letter(string):
  new_string = ""
  for index in range(0, len(string),2):
    new_string += string[index]
  return new_string

# Test
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# Reverse
# Similarly, let's write a function that receives a word parameter and return
# word in reverse.

def reverse_string(word):
  reversed_word = ""
  if word:
    for i in range(0, len(word)):
      reversed_word += word[(-1 - i)]
  return reversed_word
# Test
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# I realize I could've also written it like this:
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

# Make Spoonerism
# A Spoonerism is when you mistakenly switch the first syllables of two words like
# Jelly Beans becoming Belly Jeans. Instead of the first syllable, let's do the first letter.

def make_spoonerism(word1,word2):
  new_word1 = ""
  new_word2 = ""
  new_word1 += word2[0]
  for index in range(1,len(word1)):
    new_word1 += word1[index]
  new_word2 += word1[0]
  for index in range(1,len(word2)):
    new_word2 += word2[index]
  return new_word1 + " " + new_word2
# Test
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Later I realized I could also do this with slicing (yup, I'm a noob)
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

# Add Exclamation:
# Let's write a a program that displays a message on a large blimp. If the message is 
# greater than 20 characters, leave it as is, otherwise, fill them empty spaces with "!"
# example the message "hello" becomes "hello!!!!!!!!!!!!!!!"

def add_exclamation(word):
  if len(word) >= 20:
    return word
  else:
    longer_word = word
    while len(longer_word) < 20:
      longer_word += "!"
  return longer_word

# Test
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
print(add_exclamation("Covfefe"))
# should print Covfefe!!!!!!!!!!!!!

