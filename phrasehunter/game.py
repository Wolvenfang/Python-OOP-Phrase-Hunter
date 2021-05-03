import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("fly you fools"),
                        Phrase("you shall not pass"),
                        Phrase("a wizard is never late"),
                        Phrase("for rohan"),
                        Phrase("i am no man")]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = []

    def start(self):
        self.welcome()
        current_phrase = self.get_random_phrase()
        while True:
            current_phrase.display()
            player_guess = str(input("Guess a letter: ")) # Validation?
            self.get_guess(player_guess.lower())
            if current_phrase.check_letter(player_guess):
                current_phrase.set_letter(player_guess)
            elif player_guess.isdigit():
                print("Numbers are not a valid guess.")
            elif len(player_guess) > 1:
                print("Only 1(one) letter at a time per guess.")
            elif not current_phrase.check_letter(player_guess):
                print("Oops, missed guess. Try again.")
                self.missed += 1
                print("You have missed a total of : " + str(self.missed) + " out of 5")
            current_phrase.display()
            if current_phrase.check_complete() or self.missed == 5:
                if self.missed == 5:
                    self.game_over(False)
                    current_phrase.display_answer()
                elif current_phrase.check_complete():
                    self.game_over(True)
                play_again = input("Would you like to play again? ") # validation
                if play_again.lower() == "yes":
                    current_phrase.reset()
                    current_phrase = self.get_random_phrase()
                    self.missed = 0
                    self.guesses = []
                elif play_again.lower() == "no":
                    print("Bye! Thanks for playing!")
                    break
                else:
                    print("Not a valid option.") # How to get this to loop back if wrong.

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("Welcome to the PHRASE HUNTER game!")

    def get_guess(self, guess):
        self.guesses.append(guess)
        print("You have guessed the following: "+str(self.guesses)) #show them the guess they have made
# make the print pretty
    def game_over(self, winner):
        if winner:
            print("Well done, you have guessed the phrase correctly!")
        else:
            print("Unfortunately you have failed to guess the phrase correctly.")


test = Game()
test.start()