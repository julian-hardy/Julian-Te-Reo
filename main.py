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