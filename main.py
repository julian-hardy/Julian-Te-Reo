#Julian Hardy
#25/07/2022
#V3.2
#Importing the random library and making lists and colors
import random
print("Kia Ora, what is your name?")
name = input()
print("Welcome to my quiz " + name)
print("\n")

score = 0
red = '\033[31m'
green = '\033[32m'
white = '\033[37m'
cyan = '\033[36m'
Bpurple = '\033[1;35m'

english = ["New Zealand" , "Family" , "Food" , "Dog" , "Love"]
right_answer = ["Aotearoa" , "Whanau" , "Kai" , "Kuri" , "Aroha"]
option_1 = ["Tāmaki Makaurau" , "Waka" , "Kapai" , "Ngeru" , "Aho"]
option_2 = ["Te Whanganui a Tara" , "Iwi" , "Wai" , "Hipi" , "Hama"]
#Printing the question and making a question randomizer
def generate_question(english,right_answer,option_1,option_2):
  global score
  print(white + "What is the correct word for",english, "in te reo")
  random_sequence = random.randint(1,3)
  #Printing the options and the answers
  if(random_sequence == 1):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      print(green + "Correct!")
      score += 1
      print(cyan + "Score:", score)
    else:
      print(red + "Incorrect!")
      print(cyan + "Score:", score)

  if(random_sequence == 2):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      print(green + "Correct!")
      score += 1
      print(cyan + "Score:", score)
    else:
      print(red + "Incorrect!")
      print(cyan + "Score:", score)

  if(random_sequence == 3):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      print(green + "Correct!")
      score += 1
      print(cyan + "Score:", score)
    else:
      print(red + "Incorrect!")
      print(cyan + "Score:", score)

#Generating 5 questions and taking answers from the list
for j in range (0,5):
  generate_question(english[j],right_answer[j],option_1[j],option_2[j])

#Printing the score
print(Bpurple + "\nTotal score:", score,"\nWell done!")