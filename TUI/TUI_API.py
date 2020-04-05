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
        pass
    def game_loop(self):
        while True:
            for i in range(20):
                    print()
            self.tui.print_menu()
            uInput = input()
            if uInput == "p" or uInput == "P":
                for i in range(20):
                    print()
                self.start_game()
                time.sleep(2)
            elif uInput == "h" or uInput == "H":
                self.get_hiscores()
            elif uInput == "q" or uInput == "Q":
                for i in range(20):
                    print()
                break
            else:
                for i in range(20):
                    print()
                self.tui.print_wrong()
                time.sleep(2)

