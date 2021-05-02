import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("fly you fools"),
                        Phrase("What goood Bitch"),
                        Phrase("I hate how much work I have"),
                        Phrase("Kemuel is a bitch"),
                        Phrase("I like pugs")]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = []

    def start(self):
        self.welcome()
        current_phrase = self.get_random_phrase()
        while True:
            current_phrase.display()
            player_guess = input("Guess a letter: ") # Validation?
            self.get_guess(player_guess.lower())
            if current_phrase.check_letter(player_guess):
                current_phrase.set_letter(player_guess)
            elif not current_phrase.check_letter(player_guess):
                print("Wrong")
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
                    current_phrase = self.get_random_phrase()
                    self.missed = 0
                    self.guesses = []
                else:
                    break

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