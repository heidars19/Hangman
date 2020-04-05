from DB.DATA_API import *

def main():
    
    highscores = Highscores()
    highscores.read_file_to_datastructure()
    # data sem þarf fyrir update
    # username, win_streak, guesses, datetime.date.today()
    data = ['Heidar', '12', '22', '2020-04-04']
    # print(highscores.data_structure)
    highscores.update(data)
    # print(highscores.data_structure.top.data) # prentar út besta skorið
    # print(highscores.data_structure.top.next.data) # prentar út næst besta skorið
    
    
    # wordbank = Wordbank()
    # wordbank.read_file_to_datastructure()
    # picked_word = wordbank.random()

    # print(picked_word)
    # first_word = picked_word.split(',')
    # print(first_word[0])
    # wordbank.update(first_word[0], first_word[1:])

    return

if __name__ == "__main__":
    main()
