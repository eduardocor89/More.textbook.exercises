highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
# Separate the string into a list
print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')
print()
print(highlighted_poems_list)
print()
# strip() the whitespace for each entry
highlighted_poems_stripped = [entry.strip() for entry in highlighted_poems_list]
print(highlighted_poems_stripped)
print()
# Grab each detail from the list of details
highlighted_poems_details = [entry.split(':') for entry in highlighted_poems_stripped]
print()
print(highlighted_poems_details)
# Iterate through each detail and parse them onto the following 
# lists
titles = []
poets = []
dates = []
print() 
print("\nParsed details")
for entry in highlighted_poems_details:
  titles.append(entry[0])
  poets.append(entry[1])
  dates.append(entry[2])
print(titles)
# Write a loop that prints out 
# "The poem TITLE was published by POET in DATE"
print("\n...and finally\n")
for i in range(len(titles)):
  print("The poem {} was published by {} in {}".format(titles[i],poets[i],dates[i]))
