import random

name = "Mitsos"

question = "Is it a good day today?"

answer = ""

random_number = random.randint(1, 9)

#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Not sure"
elif random_number == 11:
  answer = "Come back tomorrow"
elif random_number == 12:
  answer = "Bah"
elif random_number == 13:
  answer = "Not quite sure"
elif random_number == 14:
  answer = "hmmm"
elif random_number == 15:
  answer = "Could be"
elif random_number == 16:
  answer = "It depends"
elif random_number == 17:
  answer = "I think yes"
elif random_number == 18:
  answer = "Are you sure about your question?"
elif random_number == 19:
  answer = "Very"
else:
  answer = "Error"

if name == "":
  print(" Asks: " + question)
else:
  print(name + " asks " + question)

if question == "":
  print("No question is provided")

if not name == "" and not question == "":
  print("Magic 8-Ball's answer: " + answer)
