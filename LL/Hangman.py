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

        self.result = False # Win or loss


    def set_max_wrong_guesses(self, number_of_guesses) :
        if number_of_guesses > 0 :
            self.max_wrong_guesses = number_of_guesses


    def print_dashline(self) :
        buffer_dashline = ""
        for letter in self.dash_line :
            buffer_dashline += letter + " "
        return buffer_dashline.strip()    
        
        

    def fill_dash_line(self, user_input) :
        
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
        
        if len(user_input) > 1 :
            self.guesses += 1
            if user_input == self.word :
                return True
            else :
                self.guesses += 1
                return False
        elif len(user_input) == 1 :
            if user_input in self.dash_line :
                return False # Returns without increasing guesses, cause it's already been guessed
            elif user_input in self.word :
                # print(" Dash line: {}".format(self.dash_line))
                self.fill_dash_line(user_input)
                # self.guesses += 1
                if user_input == self.dash_line :
                    return True # All '-' have been replaced in dash_line
                return False
            else :
                self.guesses += 1
                return False
        
            # Bogus input
        return False

    def register_results(self) :
        data = self.wordbank.find(self.word).strip('\'\n"[]').split(',')

        # print("register data: {}".format(data))

        data[0] = str(int(data[0]) + 1)
        if self.result : # True if win
            data[1] = str(int(data[1]) + 1)
        else :
            data[1] = str(int(data[1]))
        data[2] = str(int(data[2]) + self.guesses)
        self.guesses = 0
        data[3] = str(datetime.date.today())

        self.wordbank.update(self.word, data)
        # print("register data: {}".format(data))

    def print_game_end(self, win) :
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
        
        random_word = self.wordbank.random().split(',')
        self.word = self.buffer_word = random_word[0]
        self.dash_line = "_" * len(self.word)

        self.gameon = True
        while self.gameon :
            if self.word == self.dash_line:
                self.result = True
                self.gameon = False # Game over
                break
            
            print("Þú átt {} tilraunir eftir.".format(self.max_wrong_guesses - self.guesses))
            user_input = input("Guess the word: ")
            
            self.result = self.compare_sting(user_input)
            print(self.print_dashline())
            if self.guesses >= self.max_wrong_guesses :
                self.gameon = self.result = False
            
            # print("Dash line: {}".format(self.dash_line))
            # print("Word: {}".format(self.word))
        if not self.gameon :
            self.register_results()
            self.print_game_end(self.result)


    # self.play()

