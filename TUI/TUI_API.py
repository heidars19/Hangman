from LL.Hangman import Hangman
from DB.Highscores import Highscores
from TUI.TUI import TUI
import time
class API():
    def __init__(self):
        self.hang = Hangman()
        self.hi = Highscores()
        self.tui = TUI()
    def start_game(self):
        self.hang.play()
    def get_hiscores(self):
        self.hi.read_file_to_datastructure()
        
    def game_loop(self):
        while True:
            print("\n"*20)
            self.tui.print_menu()
            if self.hang.get_user() == "" :
                uInput = input("Make your choice: ")
            else :
                uInput = input(self.hang.get_user() + ": ")
            if uInput == "p" or uInput == "P":
                print("\n"*20)
                self.start_game()
                # time.sleep(2)
                input()
            elif uInput == "h" or uInput == "H":
                self.get_hiscores()
                print("\n"*20)
                self.tui.print_hiscores(self.hi.data_structure.top)
                # print_hiscores(self.hi.data_structure)
                input()
            elif uInput == "q" or uInput == "Q":
                print("\n"*20)
                break
            elif uInput == "s" or uInput == "S":
                print("\n"*20)
                username = input("Choose a username: ")
                self.hang.set_user(username)
            else:
                print("\n"*20)
                self.tui.print_wrong()
                time.sleep(2)

