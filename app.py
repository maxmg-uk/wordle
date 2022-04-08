from colorama import Back
import random

"""
Quickly thrown together wordle copy. Uses local wordlist.txt file for words. 
Length of words and amount of guesses can be easily changed. 

"""
# main loop start
while True:
    print("Start a new game? (y/quit)")
    command = input()
    if command == "quit":
        break
    # read wordlist file
    csv_file = open('wordlist.txt', 'r')
    csv_contents = csv_file.readlines()
    csv_file.close()

    # clean up words and only select the 5 letter ones
    word_list = [w.strip() for w in csv_contents if len(w.strip()) == 5]
        
    answer = random.choice(word_list)
    inner_loop = 0
    alpha = ""

    # start game loop 
    while inner_loop <= 5:
        guess = input("What is your guess? ")

        result = ""

        # loop through the letters in the guessed word, comparing to answer
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                result = result + Back.GREEN + guess[i] + Back.RESET
            elif guess[i] in answer:
                result = result + Back.YELLOW + guess[i] + Back.RESET
            else:
                result = result + guess[i] + Back.RESET
                if guess[i] not in alpha:
                    alpha = alpha + guess[i]
        
        # print the result of the guess with colour-coded letters
        print(result)
        
        # print a list of incorrectly guessed letters 
        print(''.join(sorted(alpha)))

        if answer == guess:
            print("You win")
            break

        inner_loop += 1
    
    # print the answer if they didn't get it right
    print("The answer was " + answer)
