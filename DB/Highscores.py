
from DB.FileHandlr import FileHandlr
from DB.Bucket import Bucket
import csv


class Highscores (FileHandlr):
    
    def __init__(self, data_to_append=None, update_key=None, update_with=None):
        self._filename = FileHandlr.HIGHSCORES_FILE
        self.header = FileHandlr.HIGHSCORES_HEADER
        self.data_structure = None

    def update(self, data) :
        ''' Updates a value pair corresponding to given key '''
        key = self.__get_next_id()
        self.__append_to_file(key, data)
        self.read_file_to_datastructure()
        
    def __get_next_id(self) :
        with open(self._filename, mode='rt', encoding='utf-8') as file_original :  
            reader = csv.reader(file_original, delimiter=',')
            next_id = 0
            next(reader) # Skip header
            for row in reader :
                print("Next id: {}".format(next_id))
                if next_id < int(row[0]) :
                    next_id = int(row[0])
        return str(next_id + 1)
    
    def __list_to_str(self, data) :
        ''' Converts a list into a string, before it gets written into a csv file. '''
        temp_str = ""
        for element in data :
            temp_str += "," + element.strip()
        return temp_str   
    
    def __append_to_file(self, key, data) :
        new_line = "\n" + str(key) + self.__list_to_str(data)
        print(new_line)
        with open(self._filename, 'a', encoding='UTF-8') as file_to_append_to:
            file_to_append_to.write(new_line)
                    
                    
    def read_file_to_datastructure(self) :
        ''' Reads file into Bucket structure. '''
        with open(self._filename, mode='rt', encoding='utf-8') as file_original: 
            reader = csv.reader(file_original, delimiter=',')
            header = next(reader) # Skips header row
            self.data_structure = Bucket()
            
            # reader_sorted = sorted(reader, key=lambda row: (int(row[3]), int(row[2])))
            reader_sorted = sorted(reader, key=lambda row: int(row[3]), reverse=True)
            reader_sorted2 = sorted(reader_sorted, key=lambda row: int(row[2]))
            
            for line in reader_sorted2:
                
                if len(line) > 1:
                    self.data_structure.insert(line[0], line[1:])
              
            
if __name__ == "__main__":
    bank = Highscores()
    file_stream = bank.read_filestream_into_list()
    print(bank.data_structure)