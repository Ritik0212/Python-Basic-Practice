import random
tries = 0

#word_guessing

words = ("networks", "operating", "drive", "random", "long", "time", "easy", "guess", "test", "design")

word = random.choice(words)

while tries < 5:
    guess = input("The word is " + str(len(word)) + " letters long. Guess a letter!: ")

    if guess not in word:
        print("Sorry, try again.")
    else:
        print("Nice, Guess another!")

    tries = tries + 1

    if tries == 5:
        final = input("Try to guess the word!: ")

        if final == word:
            print("Correct! My word was ", word, "!")

        else:
            print("Wrong, My word was ", word, ". Better luck next time!")
