#Hangman with preset word

word = list("apple")
strWord = "apple"
guesses = 5
winner = False
incorrectLetters = []
guess = ["_"] * len(word)

def wrong():
    global guesses
    guesses -= 1

def score():
    print("\n\nGuesses left: " + str(guesses))
    print("Incorrect Letters: ", end ="")
    for x in range(len(incorrectLetters)):
        if x == len(incorrectLetters) - 1:
            print(incorrectLetters[x], end ="")
        else:
            print(incorrectLetters[x], end =", ")
    print("")
    for x in range(len(guess)):
        if x == len(guess) - 1:
            print(guess[x], end ="")
        else:
            print(guess[x], end =",")
    print("")
            
def ask():
    letter = input("Please guess a letter: ").lower()
    correct = False
    for i in range(len(word)):
        if letter == word[i]:
            guess[i] = letter
            correct = True
    if correct:
        print(letter + " is a correct letter.")
    else:
        print("There is no " + letter)
        global guesses 
        guesses -= 1
        incorrectLetters.append(letter)
            
def check():
    if "_" not in guess:
        global winner
        winner = True
            
                
print("Let's play Hangman. You have 10 Guesses to guess the word")
while guesses > 0 and winner == False:
    score()

    ask()
    
    check()

if guesses == 0:
    print("You lost. The word is " + strWord)
else:
    if guesses == 1:
        print("Great job! You won with " + str(guesses) + " guess left!")
    else:
        print("Great job! You won with " + str(guesses) + " guesses left!")
