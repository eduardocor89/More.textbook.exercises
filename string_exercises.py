# Count without using len() function

def get_length(string):
  count = 0
  for letter in string:
    count += 1
  return count

print(get_length("iamatotalpieceofshit"))

# Write a function called letter_check() that returns
# True if the word contains the letter and False otherwise. 
# do not use 'in'

def letter_check(word,letter):
  for char in word:
    if char == letter:
      return True
  return False

print(letter_check("apple","d"))
print(letter_check("text","e"))
print(letter_check("macbook","o"))
print(letter_check("coffee","k"))

# write a function called contains() that takes two arguments
# and returns true if the sub_string can be found in the string. 
# Use in

def contains(big_string, little_string):
  if little_string in big_string:
    return True
  return False

print(contains("watermelon","melon"))

# define a function that returns a list with all of the letters
# a string_one and string_two have in common. The letters in the returned
# list should be unique. For example: 
# common_letters("banana","cream") should return ['a']

def common_letters(string_one, string_two):
  common_letters = []
  for letter in string_one:
    if letter in string_two and not letter in common_letters:
      common_letters.append(letter)
  return common_letters


print(common_letters("banana", "cream"))
print(common_letters("pepperoni","paparazzi"))

# Define a username_generator funciton that'll return
# a username as the first three letters of the first name and
# the first four letters of the last name. if the first name
# and last names are shorter than 3 characters and 4 respectively, 
# return the whole name as their username.
# Ex username_generator("Tim","Cook") returns TimCook while "Tim","Allen" returns TimAlle

def username_generator(first_name,last_name):
  if len(first_name) <= 3:
    username = first_name + last_name[:4]
  elif len(last_name) <= 4:
    username = frist_name[:3] + last_name
  elif len(first_name) <= 3 and len(last_name) <= 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username
# Define a password_generator() function that'll generate a password
# from the username string by moving the last character to the front of the string
# username = AbeSimp will return pAbeSim


# def password_generator(username):
    ''' I found two ways: this is the first one'''
#   password = username[-1] + username[:-1]
#   return password

def password_generator(username):
  '''I found two ways: this is the second one'''
  password = ''
  for index in range(len(username)):
    password += username[index - 1]
  return password 

print(username_generator("oat","latte"))
print(password_generator(username='iamatotalpieceofshit'))


