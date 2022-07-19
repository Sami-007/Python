import random
import string
from xml.sax.xmlreader import InputSource
from words import countries


def get_country(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()    

def hangman():

    word = get_country(countries)
    word_letters = set(word) # letter in word
    alphabet = set(string.ascii_uppercase) # A to z all characters 
    used_letters = set () # what the user has guessed

    lives = 6

    while len(word_letters)  > 0 and lives > 0:

         # letter already used by user
        print('You have ', lives , " lives left and you have used these letters ", ' '.join(used_letters))

         #what current word is (ie W - A R -)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('count word: ', ' '.join(word_list))

        #getting input from user
        input1 = input('Guess the letter : ').upper()
        if input1 in alphabet - used_letters:
            used_letters.add(input1)
            if input1 in word_letters:
                word_letters.remove(input1)

            else:
                lives -= 1
                print("Letter is not in the word")

        elif input1 in used_letters:
            print("You have already used that characters. Please try again")
        else:
            print("Invalid character. Please try again.")

            


hangman()