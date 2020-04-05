from DB.DATA_API import *

class Hangman :
    def __init__(self) :
        self.wordbank = Wordbank()
        self.wordbank.read_file_to_datastructure()
        self.max_wrong_guesses = 10
        self.guesses = 0
        self.word = None
        self.buffer_word = None
        self.dash_line = None
        self.gameon = False # Game in progress or game over
        self.user = None
        self.result = False # Win or loss


    def set_max_wrong_guesses(self, number_of_guesses) :
        ''' Changes maximum guesses for each game. Default is 10 '''
        if number_of_guesses > 0 and isinstance(number_of_guesses, int)  :
            self.max_wrong_guesses = number_of_guesses


    def set_user(self, user) :
        ''' Sets name for current user (username). '''
        self.user = user

    def get_user(self, user) :
        ''' Returns name for current user (username). '''
        return self.user


    def print_dashline(self) :
        ''' Prints out the dashline with '_' in place of letters yet to be guessed. '''
        buffer_dashline = ""
        for letter in self.dash_line :
            buffer_dashline += letter + " "
        return buffer_dashline.strip() 


    def fill_dash_line(self, user_input) :
        ''' Fills in dashline with guessed letter, replaces '_' with letters. '''
        for i, letter in enumerate(self.word) :
            if letter == user_input :
                buffer_word = ""
                for j, lette in enumerate(self.dash_line) :
                    if j == i :
                        buffer_word += user_input
                    else :
                        buffer_word += lette
                self.dash_line = buffer_word
        
        

    def compare_sting(self, user_input):
        ''' Checks if user input is a correct guess or not.\n
        Returns True if game has been won. '''
        if len(user_input) > 1 :
            self.guesses += 1
            if user_input == self.word :
                self.dash_line = self.word
                return True
            else :
                self.guesses += 1
                return False
        elif len(user_input) == 1 :
            if user_input in self.dash_line :
                return False # Returns without increasing guesses, cause it's already been guessed
            elif user_input in self.word :
                self.fill_dash_line(user_input)
                if user_input == self.dash_line :
                    return True # All '-' have been replaced in dash_line
                return False
            else :
                self.guesses += 1
                return False
        return False

    def register_results(self) :
        ''' Updates statistics behind a word.\n
        Updates both data structure and file. '''
        data = self.wordbank.find(self.word).strip('\'\n"[]').split(',')
        data[0] = str(int(data[0]) + 1)
        if self.result : # True if win
            data[1] = str(int(data[1]) + 1)
        else :
            data[1] = str(int(data[1]))
        data[2] = str(int(data[2]) + self.guesses)
        self.guesses = 0
        data[3] = str(datetime.date.today())

        self.wordbank.update(self.word, data)


    def print_game_end(self, win) :
        ''' Prints end-of-game splash screen, win or loose. '''
        win_str = ""
        if win :
            win_str = "#  Þú vannst, Til hamingju  #"
        else :
            win_str = "#  Þú tapaðir, gengur betur næst!  #"
        str1 = "#" * len(win_str)
        str2 = "#" +  (" " * (len(win_str)-2)) + "#"
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
        
        while self.gameon :
            self.duplicate_selection = False
            if self.word == self.dash_line:
                self.result = True
                self.gameon = False # Game over
                break
            user_input = input("Guess the word: ")
            if len(user_input) == 1:
                if user_input not in self.chr_list:
                    self.chr_list.append(user_input)
                else:
                    self.duplicate_selection = True
            for i in range(50):
                print()
            print("Þú átt {} tilraunir eftir.".format(self.max_wrong_guesses - self.guesses))
            print("Valdir stafir: " + str(self.chr_list))
            if self.duplicate_selection == False:
                self.result = self.compare_sting(user_input)
            else:
                print("Stafur nú þegar valin")
            print(self.print_dashline())
            if self.guesses >= self.max_wrong_guesses :
                self.gameon = self.result = False
            print(self.hangman_picture())
        if not self.gameon :
            self.register_results()
            self.print_game_end(self.result)


    def hangman_picture(self):
        HANGMANPICS = ['''
         
             
             
             
             
             
        =========''','''
         
             
             
             
             |
             |
        =========''','''
         
             |
             |
             |
             |
             |
        =========''','''
         +---+
             |
             |
             |
             |
             |
        =========''','''
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
        return HANGMANPICS[self.guesses]
