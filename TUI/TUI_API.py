from LL.Hangman import Hangman
from DB.Highscores import Highscores
from TUI.TUI import TUI
import time

class API():
    ''' Main programs loop control '''
    
    # Number of empty lines to print to get a fresh screen
    NUMBER_OF_EMPTY_LINES = 30 
    
    def __init__(self):
        ''' Initializes helper classes '''
        self.hang = Hangman()
        self.hi = Highscores()
        self.tui = TUI()
        
    def start_game(self):
        ''' Starts the hangman game itself '''
        self.hang.play()
        
    def get_hiscores(self):
        ''' Reads highscore file into data structure '''
        self.hi.read_file_to_datastructure()
        
    def game_loop(self):
        ''' Main fucntion of the program.\n
        Runs the loop controlling the flow throughout the game. '''
        while True:
            print("\n" * API.NUMBER_OF_EMPTY_LINES)
            self.tui.print_menu()
            if self.hang.get_user() == "" :
                uInput = input("Veldu aðgerð: ")
            else :
                uInput = input("({}) {}: ".format(self.hang.max_wrong_guesses, self.hang.get_user()))
            if uInput == "p" or uInput == "P":
                print("\n" * API.NUMBER_OF_EMPTY_LINES)
                self.start_game()
                print()
                input("Ýttu á enter til að halda áfram.")
            elif uInput == "h" or uInput == "H":
                self.get_hiscores()
                print("\n" * API.NUMBER_OF_EMPTY_LINES)
                self.tui.print_hiscores(self.hi.data_structure.top)
                print()
                input("Ýttu á enter til að halda áfram.")
            elif uInput == "q" or uInput == "Q":
                print("\n" * API.NUMBER_OF_EMPTY_LINES)
                if self.hang.get_user() == "" :
                    # get info about winstreak and guesses
                    new_highscore_line = self.hang.user_status()
                    self.hi.update(new_highscore_line)
                break
            elif uInput == "s" or uInput == "S":
                print("\n" * API.NUMBER_OF_EMPTY_LINES)
                username = input("Choose a username: ")
                self.hang.set_user(username)
                self.hang.set_max_wrong_guesses() # Resets maximum guesses to default on new user (10)
            elif uInput == "g" or uInput == "G":
                print("\n" * API.NUMBER_OF_EMPTY_LINES)
                max_guesses = input("Enter new maximum guesses (default 10): ")
                try :
                    max_guesses = int(max_guesses)
                    self.hang.set_max_wrong_guesses(max_guesses)
                except :
                    print("You have to type in a number")
                    time.sleep(2)
            else:
                print("\n" * API.NUMBER_OF_EMPTY_LINES)
                self.tui.print_wrong()
                time.sleep(2)

