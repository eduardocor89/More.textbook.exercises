tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}


# You're going to do a three card spread. 
# Create an empty dicionary called spread

spread = {}

# The first card you draw is 13, pop() the value assigned to the key 13 out of the tarot
# and assign it as the value of the 'past' key of spread
draw = tarot.pop(13)
spread['past'] = draw

# The second card you draw is 22. pop the value assigned to the key 22 out of the tarot
# dictionary and assign it as the value of the 'present' key of spread
draw = tarot.pop(22)
spread['present'] = draw

# the third draw is 10. Set it to the 'future' key of your new dictionary
draw = tarot.pop(10)
spread['future'] = draw

# Iterate through the items in the spread dictionary and for each key:value pair print a string that says
# Your key is the value card

for key, value in spread.items():
  print(f"Your {key} is the {value} card.")
