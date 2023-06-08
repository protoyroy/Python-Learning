import random
randNumber = random.randint(1,100)
guesses = 0
userGuess = None
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: ")) 
    guesses +=1
    if (userGuess == randNumber):
        print("You guessed it right")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller Number")
        else:
            print('You guessed it wrong. Enter a larger Number')

print(f"You guessed the number in {guesses} guesses")

hiscore = 0   #if hiscore.txt = not given

with open ("PROJECT/hiscore.txt", 'r') as f:
    content = f.read().strip()    #strip()  removes leading and trailing whitespace characters (spaces, tabs, and newlines) from a string
    if content:
        hiscore = int(content)

if (guesses<hiscore) or hiscore ==0:
    print("You have just broken the Hiscore")
    with open("PROJECT/hiscore.txt", "w") as f:
        f.write(str(guesses))