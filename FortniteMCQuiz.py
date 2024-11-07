x = 0
print("Welcome to the Fortnite Quiz!")
print("Question 1: In what year was Fortnite Battle Royale released?")
print("(1) 2016")
print("(2) 2017")
print("(3) 2018")
print("(4) 2019")
y = int(input())
if y == 2:
    print("Correct!")
    x = x + 1
else:
    print("Incorrect!")
print("Question 2: Which company developed Fortnite?")
print("(1) Activision")
print("(2) Epic Games")
print("(3) Ubisoft")
print("(4) Rockstar Games")
y = int(input())
if y == 2:
    print("Correct!")
    x = x + 1
else:
    print("Incorrect!")
print("Question 3: What is the in-game currency of Fortnite called?")
print("(1) V-Coins")
print("(2) VBucks")
print("(3) Fortnite Dollars")
print("(4) Battle Coins")
y = int(input())
if y == 2:
    print("Correct!")
    x = x + 1
else:
    print("Incorrect!")1
print("Question 4: What is the name of Fortnite's most famous live event?")
print("(1) The End")
print("(2) The Storm")
print("(3) Battle Royale")
print("(4) Victory Royale")
y = int(input())
if y == 1:
    print("Correct!")
    x = x + 1
else:
    print("Incorrect!")

print("Score:", x, "/4")