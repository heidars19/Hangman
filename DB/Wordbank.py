
from DB.FileHandlr import FileHandlr


class Wordbank (FileHandlr):
    ''' 
    Class for keeping Word bank in a datastructure and working with it.
    '''

    def __init__(self, data_to_append=None, update_key=None, update_with=None):
        self._filename = FileHandlr.WORDBANK_FILE
        self.header = FileHandlr.WORDBANK_HEADER
        self.data_structure = None


if __name__ == "__main__":
    bank = Wordbank()
    file_stream = bank.read_filestream_into_list()
    print(bank.data_structure)
