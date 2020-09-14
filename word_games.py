import random
import time

def chooseLetter(currentWord, pastWords):
    print("\nBot choosing letter...\n")
    time.sleep(2)
    currentWord = currentWord.upper()
    with open("scrabbleWords.txt", "r") as f:
        words = []
        for line in f:
            if len(currentWord) > 3 and line.find(currentWord) == 0 and len(currentWord) == len(line)-1:
                print("You Lose!\n")
                return ""
            else:
                if len(line) > 4 and len(line) % 2 == 0 and line.find(currentWord) == 0:
                    words.append(line)
        if not words:
                print("You're bluffing!\n\nI was thinking of the word \"" + pastWords[-1][:-1].lower() + "\"\n")
                return ""
        word = chooseWord(words, 0, pastWords)
        if not word:
            word = words[random.randint(0,len(words)-1)]
        letter = word[len(currentWord)].lower()
        currentWord = (currentWord + letter).lower()
        print("Bot selects the letter: \"" + letter + "\"\n")
        print("Current word: \"" + currentWord + "\"")
        with open("scrabbleWords.txt", "r") as f:
            words = []
            for line in f:
                 if len(currentWord) > 3 and line.find(currentWord.upper()) == 0 and len(currentWord) == len(line)-1:
                    print("\nYou Win!\n")
                    return ""
        return currentWord

def chooseWord(words, num, pastWords):
    if num == len(words)*10:
        return ""
    repeat = False
    word = words[random.randint(0,len(words)-1)]
    with open("scrabbleWords.txt", "r") as f:
        for line in f:
            if len(line) > 4 and word.find(line[:-1]) == 0 and len(word) != len(line):
                repeat = True
                break
        if repeat:
            return chooseWord(words, num+1, pastWords)
        else:
            pastWords.append(word)
            return word

print("\nWelcome to ghost!")
isRunning = True
currentWord = ""
pastWords = []
while isRunning:
    letter = input("\nChoose a letter:\n\n").lower()
    if len(letter) == 1 and ord(letter) > 96 and ord(letter) < 123:
        currentWord += letter
        print("\nYou selected the letter: \"" + letter + "\"\n")
        print("Current word: \"" + currentWord + "\"")
        currentWord = chooseLetter(currentWord, pastWords)
        if not currentWord:
            isRunning = False
    else:
        print("\nInvalid letter")
