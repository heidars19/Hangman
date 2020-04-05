
from DB.FileHandlr import FileHandlr


class Highscores :
    
    def __init__(self, data_to_append=None, update_key=None, update_with=None):
        self._filename = FileHandlr.HIGHSCORES_FILE
        self.header = FileHandlr.HIGHSCORES_HEADER
        self.data_structure = None


        
            
if __name__ == "__main__":
    bank = Highscores()
    file_stream = bank.read_filestream_into_list()
    print(bank.data_structure)