import random
import time


class HangmanGame:

    def __init__(self):
        self.words_list = ["january", "florest", "ice", "python", "garden",
                           "trip", "love", "dices", "friend", "hospital"]
        self.chosen_word = random.choice(self.words_list)
        self.correct_guesses = []
        self.wrong_guesses = []
        self.attempts = 0
        self.limit_attempts = 5
        self.player = ""

        self.start()

    def word_spaces(self):
        current_word = []
        for char in self.chosen_word:
            if char in self.correct_guesses:
                current_word.append(char)
            else:
                current_word.append('_')
        return ' '.join(current_word)

    def guesses_manager(self):
        print(self.word_spaces() + "\n" +
              "\nYou have " + str(self.limit_attempts - self.attempts) +
              " attempts left!\n")
        if self.attempts > 0:
            print("Wrong letters: " + ', '.join(self.wrong_guesses) + "\n")

    def hangman(self):
        match self.attempts:
            case 1:
                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            case 2:
                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            case 3:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
            case 4:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |      \n"
                      "__|__\n")
            case 5:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
            case _:
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")

    def guess_input(self):
        while True:
            inpt = input("Input a letter: ").lower()
            if len(inpt) != 1 or not inpt.isalpha():
                print("Input online ONE letter!\n")
            elif inpt in self.wrong_guesses or inpt in self.correct_guesses:
                print("That letter was already tried!\n")
            else:
                return inpt

    def game_manager(self):
        winner = False
        while self.attempts < self.limit_attempts:
            self.hangman()
            self.guesses_manager()
            guess = self.guess_input()
            if guess in self.chosen_word:
                self.correct_guesses.append(guess)
            else:
                print("Oops! Wrong letter. Try again!")
                self.wrong_guesses.append(guess)
                self.attempts += 1

            if len(self.correct_guesses) == len(self.chosen_word):
                winner = True
                break

        if winner:
            print("Congratulations! You guessed the word!\n")
        print(f"Game over! The chosen word was [ {self.chosen_word} ]")
        confirm = input("Would you like to play again? Y (Yes)    (N) No  :").upper()
        if confirm == 'Y':
            self.game_manager()
        else:
            print("Bye!")
            exit(1)

    def start(self):
        print("\nWelcome to Hangman game!\n")
        self.player = input("Who are you? ")
        print("Hi, " + self.player + "! Good luck!")
        time.sleep(2)
        print("The game is about to start!\n Let's play!")
        time.sleep(3)
        self.game_manager()


if __name__ == '__main__':
    game = HangmanGame()
