
from DB.FileHandlr import FileHandlr


class Wordbank (FileHandlr):
    ''' 
    '''

    def __init__(self, data_to_append=None, update_key=None, update_with=None):
        self._filename = FileHandlr.WORDBANK_FILE
        self.header = FileHandlr.WORDBANK_HEADER
        self.data_structure = None
        self.data_to_append = data_to_append
        self.update_key = update_key
        self.update_with = update_with




            
if __name__ == "__main__":
    bank = Wordbank()
    file_stream = bank.read_filestream_into_list()
    print(bank.data_structure)
