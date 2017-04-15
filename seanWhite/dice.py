''' this is my doc line comment, lets rock and roll...'''

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Guess a number: "))
  return user_guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possibilities are: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "you too high!"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is: %d" % first_roll
    sleep(1)
    print "The second roll is %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "WINNER, WINNER! VEGAN DINNER!"
      return
    elif user_guess < total_roll:
      print "You lost... how sad"
      return
roll_dice(6)