from DB.DATA_API import *


def main():
    #
    wordbank = Wordbank()
    wordbank.read_file_to_datastructure()
    picked_word = wordbank.random()


    # print(picked_word)
    # first_word = picked_word.split(',')
    # print(first_word[0])
    # wordbank.update(first_word[0], first_word[1:])


    return


if __name__ == "__main__":
    main()
