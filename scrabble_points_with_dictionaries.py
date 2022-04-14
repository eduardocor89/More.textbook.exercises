letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# In this project I'll be processing some data from a group of friends playing Scrabble
# I'll use dictionaries to organize players, words, and points.

# To map the number value of letters to their corresponding points, let's make a letter_to_point dicitonary
# Let's do it with a list comprehension.

letter_to_points = {letter:point for letter, point in zip(letters,points)}

# My letters don't take into account blank tiles. Let's add " ": 0 to our dictionary
letter_to_points[" "] = 0

# I want to make a function that'll take in a word and return how many points that word is worth. 
# Define it as score_word(word)
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total
# Let's test it out. The word Brownie should have 15 points  
#print(score_word('BROWNIE'))
# ...and it does!

# Let's say that we're playing with player1, wordNerd, Lexi Con, Prof Reader and they each have played 3 rounds already. 
# I'll create a dictionary for them too and call it player_to_words

player_to_words = {
  "player1" : ['BLUE','TENNIS','EXIT'],
  "wordNerd" : ['EARTH', 'EYES','MACHINE'],
  "Lexi Con" : ['ERASER','BELLY','HUSKY'],
  "Prof Reader" : ['ZAP','COMA', 'PERIOD']
}

# Let us get a score of how many points each player has. 
# I'll make an empty dictionary and keep a tally of how many points a player has with an empty variable.

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

# and it works!


