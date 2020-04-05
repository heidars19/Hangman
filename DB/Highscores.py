
from DB.FileHandlr import FileHandlr


class Highscores :
    
    def __init__(self, data_to_append=None, update_key=None, update_with=None):
        self._filename = FileHandlr.HIGHSCORES_FILE
        self.header = FileHandlr.HIGHSCORES_HEADER
        self.data_structure = None


    # def update_highscores() :
    #     BACKUP_FILE = self._filename +'.bak'        
    #     with open(self._filename, mode='rt') as file_original: 
    #         with open('sorted.csv', 'w') as file_bak:
    #         writer = csv.writer(file_bak, delimiter=',')
    #         reader = csv.reader(file_original, delimiter=',')
    #         next(reader) # Skips header row
            
    #         sorted2 = sorted(reader, key=lambda row: (int(row[2]), int(row[3])))        
    #         for row in sorted2:
    #             writer.writerow(row)
        

    #     with open(self._filename, 'r', encoding='utf-8') as file_original:
    #         with open(BACKUP_FILE, 'w+', encoding='utf-8') as file_bak:
    #             for line in file_original:
    #                 key_word = line.split(',')
    #                 if key_word[0].strip() == key :
    #                     file_bak.write(key + self.__list_to_str(data) + '\n')
    #                 else :
    #                     file_bak.write(line)
        
            
if __name__ == "__main__":
    bank = Highscores()
    file_stream = bank.read_filestream_into_list()
    print(bank.data_structure)