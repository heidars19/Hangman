from DB.HashMap import HashMap
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
    HIGHSCORES_FILE = 'name,winstreak,date,eitthvad,eitthvad'

    def __init__ (self) :
        pass

    def read_file_to_datastructure(self) :
        with open(self._filename, 'r', encoding='utf-8') as file_original : 
            self.data_structure = HashMap()
            for line in file_original:
                words = line.split(",")
                if len(words) > 1:
                    data = str(words[1:])
                else:
                    data = []
                self.data_structure.insert(words[0].strip(), data)
            
    def random(self) :
        ''' Pick a random word from Data Structure '''
        random_map_value = random.randint(0, self.data_structure.size - 1)
        
        if self.data_structure.list[random_map_value] != None :
            random_bucket_value = random.randint(0, len(self.data_structure.list[random_map_value]) - 1)

            word = self.data_structure.list[random_map_value].top
            if random_bucket_value > 0 :    
                for _ in range(random_bucket_value) :
                    word = word.next
            return word.key + "," + word.data.strip("[, ]")
        else :
            return self.random()
        

    
    def update(self, key, data) :
        ''' Updates a value pair corresponding to given key '''
        self.data_structure.update(key, data) # updated data structure
        self.__update_file(key, data) # updates file


    def __remove_file(self, file_to_remove) :
        try :
            if os.path.exists(file_to_remove): # Checks if .bak file exists and removes it if it does
                try :
                    os.remove(file_to_remove)
                    return True
                except:
                    return False
            else :
                raise FileNotFoundError
        except :
            return False
        
        
    def write_back(self, BACKUP_FILE) :
        try :
            with open(BACKUP_FILE, 'r', encoding='utf-8') as file_bak:
                with open(self._filename, 'w+', encoding='utf-8') as file_original:
                    for line in file_bak:
                        file_original.write(line)
        except :
            return False
        return True


    def list_to_str(data) :
        temp_str = ""
        for element in data :
            temp_str += "," + element.strip()
        return temp_str    
        
        
    def __update_file(self, key, data) :
        BACKUP_FILE = self._filename +'.bak'

        with open(self._filename, 'r', encoding='utf-8') as file_original:
            with open(BACKUP_FILE, 'w+', encoding='utf-8') as file_bak:

                for line in file_original:
                    key_word = line.split(',')
                    if key_word[0].strip() == key :
                        file_bak.write(key + FileHandlr.list_to_str(data) + '\n')
                    else :
                        file_bak.write(line)


        catch_return = self.write_back(BACKUP_FILE)  # Write back over original file
        if catch_return :
            return self.__remove_file(BACKUP_FILE)  # Remove backup file
        else :
            return catch_return
        
        
        
        