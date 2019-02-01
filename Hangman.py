#Hangman with preset word

word = "apple"
guesses = 10
print("Let's play Hangman. You have 10 Guesses to guess the word")
while guesses > 0:
    global guesses
    guesses = 10
    
    print("You have " + str(guesses) + " left!")
    guess = input("Guess a letter: \n")
  
    if guess not in word:        
        print("There's no " + guess + ".")
        guesses -= 1


    elif guess == word:
        print("Correct! The answer was apple!")
        break
    elif guess in word:
        print("Correct")
    else:
        print("You are out of guesses :(")
