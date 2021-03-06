import random

def main():

    lang = input("Hello! Pick your language (English, Deutsch lub Polski) ").lower()
    
    if lang == "english":
        name = input("Hi! What's your name? ")
        y = input("How many numbers do you want (more -> harder / default -> 100): ")
        if y == "":
            y = 100
        y = int(y)
        x = input("Choose how many chances do you want (less -> harder / default -> 10): ")
        if x == "":
            x = 10
        x = int(x)
        numberofGuesses = 0
        number = random.randint(1,y)
        y = str(y)    
        print(name + ", I am thinking of a whole number between 1 and "+ y +". Can you guess what it is?")

        while numberofGuesses < x:
            while True:
                try:
                    guess = input("Take a guess: ")
                    guess = int(guess)
                    break
                except:
                    print("That's not a number!")

            numberofGuesses = numberofGuesses + 1
            guessesLeft = x - numberofGuesses

            if guess < number:
                guessesLeft=str(guessesLeft)
                print("Too low! " + guessesLeft + " guesses left.")
            if guess > number:
                guessesLeft=str(guessesLeft)
                print("Too high! " + guessesLeft + " guesses left.")
            if guess == number:
                break
        if guess == number:
            numberofGuesses = str(numberofGuesses)
            print("Congratulations! You guessed the number in " + numberofGuesses + " tries :)")
        if guess != number:
            number = str(number)
            print("Sorry. The number I was thinking of was " + number + " :(")
        
        def decision():
            again = input("Do you want to play again? y/n ").lower()
            
            if again == "y":
                main()
            elif again == "n":
                print("Good Bye!")
                exit
            else:
                decision()

        decision()

    elif lang == "polski":
        name = input("Cześć! Jak masz na imię? ")
        y = input("Ile chciałbyś mieć liczb (więcej -> trudniej / domyślnie -> 100): ")
        if y == "":
            y = 100
        y = int(y)
        x = input("Wybierz ile chcesz mieć szans (mniej -> trudniej / domyślnie -> 10): ")
        if x == "":
            x = 10
        x = int(x)
        numberofGuesses = 0
        number = random.randint(1,y)
        y = str(y)
        print(name + ", myślę o liczbie naturalnej pomiędzy 1, a "+ y +". Czy zgadniesz jaka to jest?")

        while numberofGuesses < x:
            while True:
                try:
                    guess = input("Zgadnij: ")
                    guess = int(guess)
                    break
                except:
                    print("To nie liczba!")

            numberofGuesses = numberofGuesses + 1
            guessesLeft = x - numberofGuesses

            if guess < number:
                guessesLeft=str(guessesLeft)
                print("Za mało! Zostało " + guessesLeft + " prób.")
            if guess > number:
                guessesLeft=str(guessesLeft)
                print("Za dużo! Zostało " + guessesLeft + " prób.")
            if guess == number:
                break
        if guess == number:
            numberofGuesses = str(numberofGuesses)
            print("Gratulacje! Zgadłeś liczbę za " + numberofGuesses + ". razem :)")
        if guess != number:
            number = str(number)
            print("Niestety, ale liczba, o której myślałem to " + number + " :(")
        
        def decision():
            again = input("Czy chcesz zagrać jeszcze raz? t/n ").lower()
            
            if again == "t":
                main()
            elif again == "n":
                print("Do widzenia!")
                exit
            else:
                decision()

        decision()
           
    elif lang == "deutsch":
        name = input("Hallo! Wie heißt du? ")
        y = input("Wie viele Nummern willst du (mehr -> härter / Standard -> 100): ")
        if y == "":
            y = 100
        y = int(y)
        x = input("Wählen Sie aus, wie viele Chancen Sie wünschen (weniger -> härter / Standard -> 10): ")
        if x == "":
            x = 10
        x = int(x)
        numberofGuesses = 0
        number = random.randint(1,y)
        y = str(y)    
        print(name + ", Ich denke an eine ganze Zahl zwischen 1 und "+ y +". Können Sie sich vorstellen, was es ist?")

        while numberofGuesses < x:
            while True:
                try:
                    guess = input("Rast du mal: ")
                    guess = int(guess)
                    break
                except:
                    print("Das ist keine Nummer!")

            numberofGuesses = numberofGuesses + 1
            guessesLeft = x - numberofGuesses

            if guess < number:
                guessesLeft=str(guessesLeft)
                print("Zu niedrig! " + guessesLeft + " Vermutungen übrig.")
            if guess > number:
                guessesLeft=str(guessesLeft)
                print("Zu hoch! " + guessesLeft + " Vermutungen übrig.")
            if guess == number:
                break
        if guess == number:
            numberofGuesses = str(numberofGuesses)
            print("Herzliche Glückwünsche! Sie haben die Zahl in " + numberofGuesses + " Versuchen erraten :)")
        if guess != number:
            number = str(number)
            print("Es tut uns leid. Die Zahl, an die ich dachte, war " + number + " :(")
        
        def decision():
            again = input("Möchst du noch einmal spielen? j/n ").lower()
            
            if again == "j":
                main()
            elif again == "n":
                print("Auf Wiedersehen!")
                exit
            else:
                decision()

        decision()

    else:
        print("Wrong language! Try again")
        main()

main()