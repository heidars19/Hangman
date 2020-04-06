from DB.DATA_API import *


class Hangman:
    def __init__(self):
        self.wordbank = Wordbank()
        self.wordbank.read_file_to_datastructure()
        self.max_wrong_guesses = 10
        self.guesses = 0
        self.user_guesses = 0
        self.user_winstreak = 0
        self.word = None
        self.buffer_word = None
        self.dash_line = None
        self.gameon = False  # Game in progress or game over
        self.user = ""
        self.result = False  # Win or loss

    def set_max_wrong_guesses(self, number_of_guesses=10):
        ''' Changes maximum guesses for each game. Default is 10 '''
        if number_of_guesses > 0 and isinstance(number_of_guesses, int):
            self.max_wrong_guesses = number_of_guesses

    def set_user(self, user):
        ''' Sets name for current user (username). '''
        self.user = user

    def get_user(self):
        ''' Returns name for current user (username). '''
        return self.user

    def print_dashline(self):
        ''' Prints out the dashline with '_' in place of letters yet to be guessed. '''
        buffer_dashline = "   "
        for letter in self.dash_line:
            buffer_dashline += " " + letter
        return buffer_dashline

    def fill_dash_line(self, user_input):
        ''' Fills in dashline with guessed letter, replaces '_' with letters. '''
        for i, letter in enumerate(self.word.lower()):
            if letter == user_input:
                buffer_word = ""
                for j, lette in enumerate(self.dash_line.lower()):
                    if j == i:
                        buffer_word += user_input
                    else:
                        buffer_word += lette
                self.dash_line = buffer_word

    def compare_sting(self, user_input):
        ''' Checks if user input is a correct guess or not.\n
        Returns True if game has been won. '''
        if len(user_input) > 1:
            if user_input.lower() == self.word.lower():
                self.dash_line = self.word
                return True
            else:
                self.guesses += 1
                return False
        elif len(user_input) == 1:
            if user_input.lower() in self.dash_line.lower():
                return False  # Returns without increasing guesses, cause it's already been guessed
            elif user_input.lower() in self.word.lower():
                self.fill_dash_line(user_input)
                if user_input.lower() == self.dash_line.lower():
                    return True  # All '-' have been replaced in dash_line
                return False
            else:
                self.guesses += 1
                return False
        return False

    def user_status(self):
        ''' Returns a list of current user's statistics. '''
        return [self.user, str(self.user_winstreak), str(self.user_guesses), str(datetime.date.today())]

    def register_results(self):
        ''' Updates statistics behind a word.\n
        Updates both data structure and file. '''
        data = self.wordbank.find(self.word)

        if self.user != "":
            if self.result:  # Game won, so update results
                self.user_guesses += self.guesses
                self.user_winstreak += 1
            else:  # Game lost, so reset winstreaks
                if self.user_winstreak > 0:
                    highscores = Highscores()
                    highscores.update(self.user_status())
                self.user_guesses = 0
                self.user_winstreak = 0

        data[0] = str(int(data[0]) + 1)
        if self.result:  # True if win
            data[1] = str(int(data[1]) + 1)
        else:
            data[1] = str(int(data[1]))
        data[2] = str(int(data[2]) + self.guesses)
        self.guesses = 0
        data[3] = str(datetime.date.today())

        self.wordbank.update(self.word, data)

    def print_game_end(self, win):
        ''' Prints end-of-game splash screen, win or loose. '''
        win_str = ""
        if win:
            win_str = "    #    Þú vannst, Til hamingju    #"
        else:
            win_str = "    #    Þú tapaðir, orðið var: {}    #".format(
                self.word)
        str1 = "    " + "#" * (len(win_str)-4)
        str2 = "    " + "#" + (" " * (len(win_str)-6)) + "#"
        print(str1)
        print(str2)
        print(win_str)
        print(str2)
        print(str1)

    def play(self):
        ''' Setur leikinn af stað. Breytist líklega þegar UI verður klárað. '''
        random_word = self.wordbank.random().split(',')
        self.word = self.buffer_word = random_word[0]
        self.dash_line = "_" * len(self.word)
        self.chr_list = []
        self.gameon = True

        print("    Þú átt {} tilraunir eftir.".format(self.max_wrong_guesses))
        print(self.print_dashline())
        print()

        while self.gameon:
            self.duplicate_selection = False
            if self.word.lower() == self.dash_line.lower():
                self.result = True
                self.gameon = False  # Game over
                break
            while True:
                user_input = input(
                    "    ({})Settu inn ágiskun: ".format(self.max_wrong_guesses))
                if user_input.isalpha():
                    break
                else:
                    print("    Má bara giska á bókstafi, reyndu aftur")
                    time.sleep(2)

            if len(user_input) == 1:
                if user_input not in self.chr_list:
                    self.chr_list.append(user_input)
                else:
                    self.duplicate_selection = True
            print("\n" * 50)
            print("    Þú átt {} tilraunir eftir.".format(
                self.max_wrong_guesses - self.guesses - 1))
            print("    Valdir stafir: " + str(self.chr_list))
            if self.duplicate_selection == False:
                self.result = self.compare_sting(user_input)
            else:
                print("    Stafur nú þegar valin")
            print(self.print_dashline())
            if self.guesses >= self.max_wrong_guesses:
                self.gameon = self.result = False
            print(self.hangman_picture())
        if not self.gameon:
            self.register_results()
            self.print_game_end(self.result)

    def hangman_picture(self):
        HANGMANPICS = ['''
            
                
                
                
                
                
            =========''', '''
            
                
                
                
                |
                |
            =========''', '''
            
                |
                |
                |
                |
                |
            =========''', '''
            +---+
                |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========''']

        # if self.max_wrong_guesses > 10 :
        hangmanpic = self.guesses - self.max_wrong_guesses + 10
        if hangmanpic < 0:
            hangmanpic = 0
        return HANGMANPICS[hangmanpic]
