from replit import clear
from art import logo, vs
from game_data import data
import random

def random_accounts():
  return random.randint(0, 49)

def compare(a, b):
  if a['follower_count'] > b['follower_count']:
    return "a"
  elif b['follower_count'] > a['follower_count']:
    return "b"

a = data[random_accounts()]
b = data[random_accounts()]
score = 0
game_over = False

while not game_over:
  while a == b:
    a = data[random_accounts()]

  print(logo)
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  print(vs)
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
  
  user_choice = input("Who has more followers? Type A or B: ").lower()
  highest = compare(a, b)
  if user_choice == highest:
    score += 1
    if highest == "a":
      b = a
      a = data[random_accounts()]
    elif highest == "b":
      b = b
      a = data[random_accounts()]
    clear()
    print(f"you are Right! Your score is {score}")
  else:
    clear()
    print(f"you are Wrong! Your final score is {score}")
    game_over = True