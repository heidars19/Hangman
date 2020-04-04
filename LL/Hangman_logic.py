from DB.DATA_API import *

class Hangman :

    def __init__(self) :
        self.max_wrong_guesses = 8
        self.guesses = 0
        self.wordbank = Wordbank()
        self.wordbank.read_file_to_datastructure()

    def set_max_wrong_guesses(self, number_of_guesses) :
        if number_of_guesses > 0 :
            self.max_wrong_guesses = number_of_guesses





    def compare_sting(self, real_word,word,guess,guessed):
        guess_len = len(guess)
        if guess == real_word:
            return real_word,word
        elif guess in word:
            return self.print_word(real_word,word,guess,guessed)
        else:
            return guessed,word

    def print_word(self, real_word,word,guess,guessed):
        count_letters = word.count(guess)
        while count_letters != 0:
            start_index = word.find(guess)
            buffer_string = ""
            if guessed.count(guess) < real_word.count(guess):
                # guessed = guessed[:start_index] + guess + guessed[start_index + len(guess)-1:-1]

                if start_index == 0:
                    guessed = guess+guessed[len(guess):]
                else:
                    print(guessed[start_index:start_index+len(guess)])
                    buffer_string = guessed[start_index:start_index+len(guess)].replace("_",guess,1)
                    print(buffer_string)
                    guessed = guessed[0:start_index] + buffer_string + guessed[start_index+len(guess):]
            guessed = guessed[:len(real_word)]
            word = word.replace(guess,"_"*len(guess),len(guess))
            count_letters -= 1
        return guessed,word

    def play(self):
        random_word = self.wordbank.random().split(',')
        word = buffer_word = random_word[0]
        guessed = "_"*len(word)
        while True:
            if word == guessed:
                break
            guess = input("guess the word: ")
            guessed,buffer_word = self.compare_sting(word,buffer_word,guess,guessed)
            print(guessed)
            print(buffer_word)

    # self.play()

