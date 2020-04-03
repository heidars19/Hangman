from DB.FileHandlr import FileHandlr


class Wordbank (FileHandlr) :
    ''' 

    '''
    
    def start(self) :
        if self.data_to_append :
            FileHandlr.append_data_to_file(self)
        
        elif self.line_to_replace : 
            FileHandlr.change_line_in_file(self)

        elif self.fieldname:
            self.line_number = FileHandlr.does_line_exists(self)
            return self.line_number

        else :
            FileHandlr.read_filestream_into_list(self)
            return self.data_list

        return


    def __init__ (self, data_to_append=None, fieldname=None, searchparam=None, line_to_replace=None, replace_with=None ):
    
        self.filename = FileHandlr.STAFF_TABLE
        self.header = FileHandlr.STAFF_TABLE_HEADER
        self.data_to_append = data_to_append
        self.fieldname = fieldname
        self.searchparam = searchparam
        self.line_to_replace = line_to_replace
        self.replace_with = replace_with
        self.filestream = None


 buck = Bucket()
    buck.insert(10, "lol")
    buck.insert(11, "lel")
    buck.update(11, "lop")