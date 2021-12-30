import random
from art import logo, vs
from game_data import data
from replit import clear

def check_answer(oa,ob,userC):
  if userC == 'a':
    if oa > ob :
      return True
    elif oa < ob  :
      return False
  elif userC == 'b':
    if oa > ob :
      return False
    elif oa < ob  :
      return True
  
  if oa > ob:
    return userC == 'a'
  else:
    return userC == 'b'


def compare_choices():
  print(logo)
  print(f"Compare A: {opA['name']}, {opA['description']}, {opA['country']}.")
  print(vs)
  print(f"Compare B: {opB['name']}, {opB['description']}, {opB['country']}.")
  return input("Who has more followers? Type 'A' or 'B': ")

score = 0
opA = random.choice(data)
opB = random.choice(data)

while True:

  user_choice = compare_choices()

  if user_choice == 'a':
    print("a")
    play_again = check_answer(opA['follower_count'],opB['follower_count'],user_choice)
  elif user_choice == 'b':
    print("")  
    play_again = check_answer(opA['follower_count'],opB['follower_count'],user_choice)

  if play_again == False:
    print(f"Sorry that's wrong. Final score : {score}")
    break
  else:
    score +=1
    opA = opB
    opB = random.choice(data)
    print(f"You are right. Your score : {score}")
    clear()

