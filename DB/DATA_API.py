from DB.Wordbank import Wordbank
from DB.FileHandlr import FileHandlr
from DB.Highscores import Highscores
import time
import datetime

'''
USAGE

    wordbank = Wordbank()
    wordbank.read_file_to_datastructure()
    
    picked_word = wordbank.random()
    # returns a single string randomly chosen on the form:
    þrenningarmaðra,'', '', '', '\n'
    
    
    #update a words statistics
    first_word = picked_word.split(',')
    wordbank.update(first_word[0], first_word[1:])



'''