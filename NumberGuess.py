import random
from typing import Counter

try:
    import lightrun
    lightrun.enable(company_key='c0d7ceb1-d646-41f4-956b-60a20078f09b')
except ImportError as e:
    print("Error importing Lightrun: ", e)

print("Modes:")
print("1 - Hard")
print("2 - Easy")
trycount = 0
mode = int(input())

def hardMode():
	num = random.randint(10000,99999)
	urmom = (random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9))
	print("Guess the number")
	print(num)
	done = False
	wrongCount = 0
	while done != True:
		
		guess = int(input("Guess:   "))
		guesslist = list(str(guess))
		urmom2 = list(str(num))
		numCorrect = 0
		if guess != num:
			wrongCount = wrongCount + 1
			print("You got", numCorrect, "correct")
		else:
			print("You got it right!")
			print("You failed", wrongCount, "times")
			break
		while len(str(guess)) != 5:
			print("Invalid count of numbers")
			easyMode()
			break
		else:
#			print(guesslist, "guesslist")
#			print(urmom2, "urmom2")
			rml = 0
			for c in range(0,5):
	
				if guesslist[rml] in urmom2:
					if guesslist[rml] in urmom2[rml]:
					#	print("number", guesslist[rml], "is in correct position")
						numCorrect = numCorrect + 1
					else:
					#	print("number", guesslist[rml], "is in the wrong position")
						rml = rml + 1
				else:
					rml = rml + 1


def easyMode():
	num = random.randint(1000,9999)
	urmom = (random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9))
	print("Guess the number")
	print(num)
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
			print(guesslist[0])
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


## For http://www.ocr.org.uk/Images/202838-20-code-challenges.pdf
