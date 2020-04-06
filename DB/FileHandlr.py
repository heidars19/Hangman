from DB.HashMap import HashMap
from DB.Bucket import Bucket
import csv
import fileinput
import datetime
import os
import random


class FileHandlr:
    ''' Abstract class for filehandling '''

    WORDBANK_FILE = "./Data/Wordbank.txt"
    WORDBANK_HEADER = 'word,used,wins,guesses,last_played'

    HIGHSCORES_FILE = "./Data/Highscores.txt"
    HIGHSCORES_HEADER = 'id,username,winstreak,guesses,date'

    def __init__(self):
        pass

    def find(self, key):
        ''' Given word, will return corresponding 'data'. '''
        return self.data_structure.find(key)

    def read_file_to_datastructure(self):
        ''' Reads file into HashMap structure. '''
        with open(self._filename, mode='rt', encoding='utf-8') as file_original:
            reader = csv.reader(file_original, delimiter=',')
            header = next(reader)  # Skips header row
            self.data_structure = HashMap()
            for line in reader:
                if len(line) > 1:
                    self.data_structure.insert(line[0], line[1:])

    def random(self):
        ''' Pick a random word from Data Structure '''
        random_map_value = random.randint(0, self.data_structure.size - 1)

        if self.data_structure.list[random_map_value] != None:
            random_bucket_value = random.randint(
                0, len(self.data_structure.list[random_map_value]) - 1)
            word = self.data_structure.list[random_map_value].top
            if random_bucket_value > 0:
                for _ in range(random_bucket_value):
                    word = word.next
            return word.key + "," + str(word.data).strip("[']")
        else:
            return self.random()

    def update(self, key, data):
        ''' Updates a value pair corresponding to given key '''
        self.data_structure.update(key, data)  # updated data structure
        self.__update_file(key, data)  # updates file

    def __remove_file(self, file_to_remove):
        ''' Removes a file. '''
        try:
            # Checks if .bak file exists and removes it if it does
            if os.path.exists(file_to_remove):
                try:
                    os.remove(file_to_remove)
                    return True
                except:
                    return False
            else:
                raise FileNotFoundError
        except:
            return False

    def write_back(self, BACKUP_FILE):
        ''' Writes 1 file over another.\n
        Overwrites ogininal file with Backup_file,\n
        then initiates deletion of backup_file. '''
        try:
            with open(BACKUP_FILE, 'r', encoding='utf-8') as file_bak:
                with open(self._filename, 'w+', encoding='utf-8') as file_original:
                    for line in file_bak:
                        file_original.write(line)
        except:
            return False
        return True

    def __list_to_str(self, data):
        ''' Converts a list into a string, before it gets written into a csv file. '''
        temp_str = ""
        for element in data:
            temp_str += "," + element.strip()
        return temp_str

    def __update_file(self, key, data):
        ''' Updates file, changes 1 line where 'key' dictates, with 'data'. '''
        BACKUP_FILE = self._filename + '.bak'
        with open(self._filename, mode='rt', encoding='utf-8') as file_original:
            with open(BACKUP_FILE, 'w', encoding='utf-8', newline='') as file_bak:
                writer = csv.writer(file_bak, delimiter=',')
                reader = csv.reader(file_original, delimiter=',')
                header = next(reader)  # Skips header row
                writer.writerow(header)  # Writes header at top

                for line in reader:
                    if line[0].strip() == key:
                        data.insert(0, key)
                        writer.writerow(data)
                    else:
                        writer.writerow(line)

        # Write back over original file
        catch_return = self.write_back(BACKUP_FILE)
        if catch_return:
            return self.__remove_file(BACKUP_FILE)  # Remove backup file
        else:
            return catch_return
