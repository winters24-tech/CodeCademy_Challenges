import random

name = "MJ"
question = ("Will I be great at basketball?")
answer = " "

random_number = random.randint(1, 9)
# randint (random integer) provides random selection of numbers 1-9. 1 and 9 (inclusive)



if random_number == 1:
  answer = "Yes-definitely"
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
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  print("Error")


print("        The Power of the Ball!  ")

if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

print("Magic 8-ball says: " + answer)

