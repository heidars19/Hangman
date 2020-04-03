from HashMap import HashMap
from FileHandlr import FileHandlr


class Wordbank (FileHandlr):
    ''' 

    '''

    # def start(self) :
    #     if self.data_to_append :
    #         FileHandlr.append_data_to_file(self)

    #     elif self.line_to_replace :
    #         FileHandlr.change_line_in_file(self)

    #     elif self.fieldname:
    #         self.line_number = FileHandlr.does_line_exists(self)
    #         return self.line_number

    #     else :
    #         FileHandlr.read_filestream_into_list(self)
    #         return self.data_list

    #     return

    def __init__(self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None):

        self.filename = "./Data/Wordbank.txt"
        self.header = ""
        self.data_to_append = data_to_append
        self.fieldname = fieldname
        self.searchparam = searchparam
        self.line_to_replace = line_to_replace
        self.replace_with = replace_with
        self.filestream = None

    def open_file(self):
        ''' 
        Opens a file and returns a filestream, or None if error.
        Does not close the file!
        '''
        try:
            f = open(self.filename, 'r', encoding='UTF-8')
            return f
        except:
            return None

    def read_filestream_into_list(self):
        '''
        Takes a filestream, returns a list with file contents.
        Closes the file after reading it.
        '''
        self.filestream = self.open_file()
        if not self.filestream:
            return None

        self.data_list = HashMap()
        for line in self.filestream:
            words = line.split(",")
            if len(words) > 1:
                data = ""
                for i in range(1, len(words)):
                    data += "," + words[i]
            else:
                data = ""
            self.data_list.insert(words[0], data)
            # data_list.append(line.strip())

        self.filestream.close()  # Closes file after grabbing data from it


if __name__ == "__main__":
    bank = Wordbank()
    file_stream = bank.read_filestream_into_list()
    print(bank.data_list)
