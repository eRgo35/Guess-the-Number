import random

import langs.en_US as en
import langs.de_DE as de
import langs.pl_PL as pl
            
def replay():
    while True:
        play = input(lang_play_again).lower()

        if play == "y":
            main()
        elif play == "n":
            print(lang_good_bye)
            break
        else:
            continue

def main():
    numbers = input(lang_numbers)

    if numbers == "":
        numbers = 100

    numbers = int(numbers)
    chances = input(lang_chances)

    if chances == "":
        chances = 10

    chances = int(chances)
    numberofGuesses = 0
    number = random.randint(1, numbers)

    print(name + lang_think_one + str(numbers) + lang_think_two)

    while numberofGuesses < chances:
        while True:
            try:
                guess = input(lang_guess)
                guess = int(guess)
                break
            except:
                print(lang_nan)
        
        numberofGuesses += 1
        guessesLeft = chances - numberofGuesses

        if guess < number:
            print(lang_too_low + str(guessesLeft) + lang_guesses_left)
        elif guess > number:
            print(lang_too_high + str(guessesLeft) + lang_guesses_left)
        elif guess == number:
            break

    if guess == number:
        print(lang_congratz_one + str(numberofGuesses) + lang_congratz_two)
    elif guess != number:
        print(lang_lose_one + str(number) + lang_lose_two)

while True:
    lang = input("Hello! Pick your language (English, Deutsch or Polski) ").lower()

    if lang == "english":
        lang_name = en.en_US["en_name"]
        lang_numbers = en.en_US["en_numbers"]
        lang_chances = en.en_US["en_chances"]
        lang_think_one = en.en_US["en_think_one"]
        lang_think_two = en.en_US["en_think_two"]
        lang_guess = en.en_US["en_guess"]
        lang_nan = en.en_US["en_nan"]
        lang_too_low = en.en_US["en_too_low"]
        lang_too_high = en.en_US["en_too_high"]
        lang_guesses_left = en.en_US["en_guesses_left"]
        lang_congratz_one = en.en_US["en_congratz_one"]
        lang_congratz_two = en.en_US["en_congratz_two"]
        lang_lose_one = en.en_US["en_lose_one"]
        lang_lose_two = en.en_US["en_lose_two"]
        lang_play_again = en.en_US["en_play_again"]
        lang_good_bye = en.en_US["en_good_bye"]
        break

    elif lang == "deutsch":
        lang_name = de.de_DE["de_name"]
        lang_numbers = de.de_DE["de_numbers"]
        lang_chances = de.de_DE["de_chances"]
        lang_think_one = de.de_DE["de_think_one"]
        lang_think_two = de.de_DE["de_think_two"]
        lang_guess = de.de_DE["de_guess"]
        lang_nan = de.de_DE["de_nan"]
        lang_too_low = de.de_DE["de_too_low"]
        lang_too_high = de.de_DE["de_too_high"]
        lang_guesses_left = de.de_DE["de_guesses_left"]
        lang_congratz_one = de.de_DE["de_congratz_one"]
        lang_congratz_two = de.de_DE["de_congratz_two"]
        lang_lose_one = de.de_DE["de_lose_one"]
        lang_lose_two = de.de_DE["de_lose_two"]
        lang_play_again = de.de_DE["de_play_again"]
        lang_good_bye = de.de_DE["de_good_bye"]
        break

    elif lang == "polski":
        lang_name = pl.pl_PL["pl_name"]
        lang_numbers = pl.pl_PL["pl_numbers"]
        lang_chances = pl.pl_PL["pl_chances"]
        lang_think_one = pl.pl_PL["pl_think_one"]
        lang_think_two = pl.pl_PL["pl_think_two"]
        lang_guess = pl.pl_PL["pl_guess"]
        lang_nan = pl.pl_PL["pl_nan"]
        lang_too_low = pl.pl_PL["pl_too_low"]
        lang_too_high = pl.pl_PL["pl_too_high"]
        lang_guesses_left = pl.pl_PL["pl_guesses_left"]
        lang_congratz_one = pl.pl_PL["pl_congratz_one"]
        lang_congratz_two = pl.pl_PL["pl_congratz_two"]
        lang_lose_one = pl.pl_PL["pl_lose_one"]
        lang_lose_two = pl.pl_PL["pl_lose_two"]
        lang_play_again = pl.pl_PL["pl_play_again"]
        lang_good_bye = pl.pl_PL["pl_good_bye"]
        break
    
    else:
        print("Wrong language! Try again")
        continue

name = input(lang_name)
main()
replay()    