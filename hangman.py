"""
Hangman Game
"""
import random

#declare variables needed
animals = ["tiger","lion","swan","bear","wolf"]
answer = [] #to store our answer later
used = [] #to store our letters that already used
lives = 5
score = 0 

def printHeart(x):
  counter = 0
  hearts = ""
  #loop to print the hearts
  while counter < x:
    hearts = hearts + u'\u2764' #<= unicode to create an emoji heart in Python
    counter += 1
  print(hearts + "(" + str(x) + "lives)")

def set_blanks(new_animal):
  counter = 0 
  while counter < len(new_animal):
    answer.append("_")
    counter += 1

def checkLength(char):
  if len(char) == 1:
    return True
  else:
    return False

def checkUsed(letter,used):
  for x in used:
    if x == letter:
      return False
    return True

def checkAnswer(new_animal, letter, blanks):
  added_score = 0
  for index, val in enumerate(new_animal):
    if letter == val:
      added_score += 1
      blanks[index] = letter
  used.append(letter)
  return added_score

new_animal = random.choice(animals)
req_score = len(new_animal)

#call the set set_blanks
set_blanks(new_animal)

#intro statement 
print("Welcome to Hangman Game. The idea is animals.")
print("Remember to keep your 5 lives to win the game!")

#main game loop
while True:
  print("n\Lives: ")
  printHeart(lives)
  print("\nAnimal name so far:\n" + str(answer))
  print("\nUsed letters:\n" + str(used))

  #variable input answer
  inptAnswer = input("\nPlease guess a better letter here: ").lower()

  print("=======================================================")
  #condition to checking our input is only 1 letter
  if checkLength(inptAnswer):
    if checkUsed(inptAnswer, used):
      addScore = checkAnswer(new_animal, inptAnswer, answer)
      score += addScore
      if addScore == 0:
        lives -= 1
        print("\nYou've lost a live!")
      else:
        print("\nYay! Your input is right!")
    else:
      print("\nYou've already used that letter! Try again!")
  else:
    print("Invalid Input")
    
#condition for win or lose
  if lives == 0:
    print("\nGame Over")
    break
  if score == req_score:
    print("\nYou win!")
    break
