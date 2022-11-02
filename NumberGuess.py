import random

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
        easyMode()
        break
    else:
        print(guesslist)
        print(urmom2)
        print(guesslist[0])
        thing = 0
        for c in range(0,4):
            if guesslist[thing] in urmom2:
                print("number is in", guesslist[thing])
                thing = thing + 1
                break
            else:
                print("no")
                thing = thing + 1
                break


if mode == 1:
    hardMode()

if mode == 2:
    easyMode()