#DiceRoll.py
#Name: Macy Dubes
#Date: 10/5/2025
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  numTrials = 10000
  #Create two dice values ranging from 1 - 6 each
  for r in range(numTrials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    rolls[total - 2] = rolls[total - 2] + 1
  #find the sum total of the two dice
  #print statictics for dice rolls
  print("Dice Roll Statistics (Total Rolls:", numTrials, ")")
  diceSum = 2
  numTrialsFloat = float(numTrials)
  for count in rolls:
    percentageUnrounded = (count / numTrialsFloat) * 100
    percentage = round(percentageUnrounded, 2)
    print(diceSum, ":", count, "rolls (", percentage, "%)")
    diceSum = diceSum + 1

if __name__ == '__main__':
  main()
