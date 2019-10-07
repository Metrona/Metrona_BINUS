#%%
def hangman():
    word = str(input("word: "))
    spaces = "_ "*len(word)
    print (spaces)
    wrong = 0
    guesses = ""
    print("type quit in when guess")
    while True:
        if "_ " in spaces:
            guess = str(input("guess: "))
            if guess in word and guess not in guesses:
                for x in range(0,len(word),1):
                    if word[x] == guess:
                        templ = spaces.split(" ")
                        templ[x] = guess
                        temps = ""
                        for element in templ:
                            temps = temps + element + " "
                        spaces = temps
                print (spaces)
                guesses = guesses + guess + " "
            elif guess == "quit":
                return False
            elif wrong == 5:
                return False
            elif guess in guesses:
                print("you already guessed that")
            else:
                print(guess, "not found")
                wrong += 1
                guesses = guesses + guess + " "
            print (guesses)               
        else:
            print("You Win!")
            return False