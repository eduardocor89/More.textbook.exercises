# Exercises for accessing lists with indices

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["pysics", "calculus", "poetry", "history"]
grades = [98,97,85,88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#print(gradebook)
gradebook.append(["computer science", 100])
#print(gradebook)
gradebook.append(["visual arts", 93])
print(gradebook)
gradebook[-1][-1] = 98
print(gradebook[-1][-1])
gradebook[2].remove(gradebook[2][-1])
gradebook[2].append("Pass")
print(gradebook[2])

full_gradebook = last_semester_gradebook + gradebook
print()
print(full_gradebook)

