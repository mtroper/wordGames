import random
import time

def chooseLetter(currentWord):
    print("\nBot choosing letter...\n")
    time.sleep(2)
    currentWord = currentWord.upper()
    with open("scrabbleWords.txt", "r") as f:
        words = []
        for line in f:
            if len(currentWord) > 4 and line == currentWord:
                print("You Lose!\n")
                return ""
            else:
                if len(line) > 4 and len(line) % 2 == 0 and line.find(currentWord) == 0:
                    words.append(line)
        if not words:
                print("You're bluffing!\n")
                return ""
        elif len(words) == 1:
            print("You win!\n")
            return ""
        word = words[random.randint(0,len(words))]
        print(word)
        letter = word[len(currentWord)].lower()
        currentWord = (currentWord + letter).lower()
        print("Bot selects the letter: \"" + letter + "\"\n")
        print("Current word: \"" + currentWord + "\"")
        return currentWord

print("\nWelcome to ghost!")
isRunning = True
currentWord = ""
while isRunning:
    letter = input("\nChoose a letter:\n\n").lower()
    if len(letter) == 1 and ord(letter) > 96 and ord(letter) < 123:
        currentWord += letter
        print("\nYou selected the letter: \"" + letter + "\"\n")
        print("Current word: \"" + currentWord + "\"")
        currentWord = chooseLetter(currentWord)
        if not currentWord:
            isRunning = False
    else:
        print("\nInvalid letter")
