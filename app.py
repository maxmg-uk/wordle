import nltk
from nltk.corpus import words
from colorama import Back
import random

"""


"""

# Run this once to download wordlist file 
nltk.download()

while True:
    print("Start a new game? (y/quit)")
    command = input()
    if command == "quit":
        break

    word_list = [w for w in words.words() if len(w) == 5]
    answer = random.choice(word_list)
    inner_loop = 0
    alpha = ""

    while inner_loop < 11:
        guess = input("What is your guess? ")

        result = ""

        for i in range(len(answer)):
            if guess[i] == answer[i]:
                result = result + Back.GREEN + guess[i] + Back.RESET
            elif guess[i] in answer:
                result = result + Back.YELLOW + guess[i] + Back.RESET
            else:
                result = result + guess[i] + Back.RESET
                if guess[i] not in alpha:
                    alpha = alpha + guess[i]

        print(result)
        print(''.join(sorted(alpha)))

        if answer == guess:
            print("You win")
            break

        inner_loop += 1

    print("The answer was " + answer)
