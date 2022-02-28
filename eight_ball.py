import random

name = "eddie"
question = "Will I win the lottery?"
answer = ""

random_number = random.randint(1,11)

if random_number == 1:
  answer = "Yes- definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
 answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
  answer = "If you set your mind to it"
elif random_number == 11:
  answer = "It will come to you, but you must be patient" 
else:
  answer = "Error"

if name == "":
  name = "Question: "
else:
  name = name.title() + " asks:"

if len(question) == 0:
  print("You haven't asked a question. Ask away")
else:
  print(name + " " + question)
  print("Magic 8-Ball's answer: " + answer)



