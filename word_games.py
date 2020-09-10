def chooseLetter(currentWord):
    print("Bot chooses the letter")

with open("scrabbleWords.txt", "r") as f:
        print("\nWelcome to ghost!")
        isRunning = True
        currentWord = ""
        while isRunning:
            letter = input("\nChoose a letter:\n\n").lower()
            if len(letter) == 1 and ord(letter) > 96 and ord(letter) < 123:
                currentWord += letter
                print("\nYou selected the letter: \"" + letter + "\"\n")
                print("Current word: \"" + currentWord + "\"")
                chooseLetter(currentWord)
            else:
                print("\nInvalid letter")
