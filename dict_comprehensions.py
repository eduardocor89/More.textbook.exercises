# Let's build a music streaming sercice where
# each list represents songs in a user's library and the amount
# of times each song has been played. 

# Use a dictionary comprehension to create a dict called plays that zips all of this
# information together
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs,playcounts)}
print(plays)

# Add a new entry to it "Purple Haze" with only 1 playcount
plays["Purple Haze"] = 1

# Aretha Frankli's 'Respect' is a banger. Update it with a counter up to 94
plays["Respect"] = 94

# Create a dictionary called Library that has two key:value pairs
# "The Best Songs" with a value of plays
# "Sunday Feelings" with a value of empty dicitonary
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)
