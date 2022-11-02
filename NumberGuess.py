import random

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
    print("Guess the number")
    guess = int(input(""))


def easyMode():
	num = random.randint(1000,9999)
	urmom = (random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9))
	print("Guess the number")
	print(num)
	guess = int(input())
	guesslist = list(str(guess))
	urmom2 = list(str(num))
	while len(str(guess)) != 4:
		print("Invalid count of numbers")
		easyMode()
		break
	else:
		print(guesslist, "guesslist")
		print(urmom2, "urmom2")
		print(guesslist[0])
		rml = 0
		for c in range(0,4):
			if guess == num:
				print("You got it!")
				break

			if guesslist[rml] in urmom2:
				if guesslist[rml] in urmom2[rml]:
					print("number", guesslist[rml], "is in correct position")
				else:
				##	print("number", guesslist[rml], "is in position", (rml + 1))
					print("number", guesslist[rml], "is in the wrong position")
				rml = rml + 1
				
			else:
				print("no")
				rml = rml + 1
            
            


if mode == 1:
    hardMode()

if mode == 2:
    easyMode()