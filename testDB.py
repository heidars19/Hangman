from DB.DATA_API import *


def main():
    #
    wordbank = Wordbank()
    wordbank.read_file_to_datastructure()
    picked_word = wordbank.random()


    data = ['1','1','7','12.03.2020']
    print(picked_word)
    wordbank.update(picked_word, data)

    print(wordbank.data_structure)

    return


if __name__ == "__main__":
    main()
