import random

totalDice = int(input('Total No of Dices : '))

totalSides = int(input('Total Sides : '))

dices_values = [None] * totalDice

diceNumber = 1

for dice in dices_values:
    dice = random.randrange(1,totalSides+1)
    print('Dice ',diceNumber,' is :' , dice)
    diceNumber=diceNumber+1
















# print ("TOTAL DICES : "+totalDice)
# print ("Total Sides : "+totalSides)