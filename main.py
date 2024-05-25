# Display art
from art import logo, vs
from game_data import data
import random
from replit import clear

# '''Format the account data into printable format'''

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  account_follower = account["follower_count"]
  return (f"{account_name}, a {account_descr}, from {account_country}")
  
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == 'b'
  
print (logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make game repeatable

while game_should_continue:

  
  # Generate a random account from the game data
  
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
    
  print(f"Compare A: {format_data(account_a)},")
  print(vs)
  print(f"Against B: {format_data(account_b)},")
  
  # Ask user for a guess
  guess = input("Who has more followers? Type 'A or 'B:").lower()
  # Get follower count of each account
  # Check if user is correct 
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  # Use if statement to check if user is correct
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  # Give user feedback on their guess
  # Score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")

# Making account at position B become the next account at position
