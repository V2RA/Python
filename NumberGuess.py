import random
from typing import Counter

print("Modes:")
print("1 - Hard (5 digits)")
print("2 - Easy (4 digits)")
print("3 - Description for both")
trycount = 0
mode = int(input())

if mode == 3:
	print("Hard mode is 5 digits, and only shows how many you got right; not which ones you got right and which position")
	print("Easy mode is 4 digits, and shows which number you got right")
	mode = int(input("Choose:   "))

def hardMode():
	num = random.randint(10000,99999)
	urmom = (random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9))
	print("Guess the number")
	done = False
	wrongCount = 0
	while done != True:
		guess = int(input("Guess:   "))
		guesslist = list(str(guess))
		urmom2 = list(str(num))
		numCorrect = 0
		while len(str(guess)) != 5:
			print("Invalid count of numbers")
			hardMode()
			break
		else:
			rml = 0
			for c in range(0,5):
				if guesslist[rml] in urmom2:
					if guesslist[rml] in urmom2[rml]:
						numCorrect = numCorrect + 1
						rml = rml + 1
					else:
						rml = rml + 1
				else:
					rml = rml + 1
		if guess != num:
			wrongCount = wrongCount + 1
			print("You got", numCorrect, "correct")
		else:
			print("You got it right!")
			print("You failed", wrongCount, "times")
			break



def easyMode():
	num = random.randint(1000,9999)
	urmom = (random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9))
	print("Guess the number")
	done = False
	wrongCount = 0
	while done != True:
		guess = int(input("Guess:   "))
		guesslist = list(str(guess))
		urmom2 = list(str(num))
		if guess != num:
			wrongCount = wrongCount + 1
		else:
			print("You got it right!")
			print("You failed", wrongCount, "times")
			break
		while len(str(guess)) != 4 and guesslist[0] != "0":
			print("Invalid count of numbers")
			easyMode()
			break
		else:
			rml = 0
			for c in range(0,4):
				if guesslist[rml] in urmom2:
					if guesslist[rml] in urmom2[rml]:
						print("number", guesslist[rml], "is in correct position")
					else:
						print("number", guesslist[rml], "is in the wrong position")
					rml = rml + 1
				else:
					rml = rml + 1


if mode == 1:
    hardMode()

if mode == 2:
    easyMode()

print("Would you like to go again?")
goA = input()
goAgain = goA.lower()
if goAgain == "yes":
	print("Which one?")
	print("Modes:")
	print("1 - Hard (5 digits)")
	print("2 - Easy (4 digits)")
	nall = int(input())
	if nall == 1:
		hardMode()
	if nall == 2:
		easyMode()


## For http://www.ocr.org.uk/Images/202838-20-code-challenges.pdf