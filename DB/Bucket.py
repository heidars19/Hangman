from Errors import *


class Bucket():
    class SLL():
        def __init__(self, Key=None, Data=None, Next=None):
            self.key = Key
            self.data = Data
            self.next = Next

    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        output_string = ""
        buffer_node = self.top
        while buffer_node != None:
            output_string += "key: " + \
                str(buffer_node.key).strip() + " data: " + \
                str(buffer_node.data).strip() + "\n"
            buffer_node = buffer_node.next
        return output_string

    def insert(self, key, data):
        ''' Creates a new SSL to hold the data, or appends data to an existing SSL if there is any. '''
        if self.top == None:
            self.top = self.SLL(key, data, self.top)
        else:
            self._loopdy_loop(key, data, "insert")
        self.size += 1

    def _loopdy_loop(self, key=None, data=None, state=None):
        buffer_node = self.top
        while buffer_node != None:
            if buffer_node.key == key:
                if state == "insert":
                    raise ItemExistsException()
                elif state == "update" or state == "set":
                    buffer_node.data = data
                    return True
                elif state == "find":
                    return buffer_node.data
                elif state == "contains":
                    return True
            if state == "remove":
                if buffer_node.next.key == key:
                    buffer_node.next = buffer_node.next.next
                    self.size -= 1
                    return
            buffer_node = buffer_node.next
        if state == "update" or state == "find" or state == "remove":
            raise NotFoundException
        elif state == "contains":
            return False
        elif state == "set" or state == "insert":
            self.top = self.SLL(key, data, self.top)

    def update(self, key, data):
        ''' Updates an existing key with new value, raises NotFoundException if 'key' doesn't exist '''
        self._loopdy_loop(key, data, "update")

    def find(self, key):
        ''' Find key and returns it's value. Raises NotFoundException if 'key' doesn't exist '''
        return self._loopdy_loop(key, state="find")

    def contains(self, key):
        ''' Returns True if 'key' exists, else False '''
        return self._loopdy_loop(key, state="contains")

    def remove(self, key):
        ''' Removes the value pair with key from the collection.\n
        If key is not in the collection, raise NotFoundException '''
        if self.top.key == key:
            self.top = self.top.next
            self.size -= 1
        else:
            self._loopdy_loop(key, state="remove")

    def __setitem__(self, key, data):
        ''' If  key exists in the collection, update its data value\n
        Otherwise add the value pair to the collection\n
        Allows for 'collection[key] = data' for both updating and inserting new values '''
        if not self._loopdy_loop(key, data, state="set"):  # Returns true if it updates, None if new insert
            self.size += 1

    def __getitem__(self, key):
        ''' Returns the data value of the value pair with equal key\n
        If key is not in the collection, raise NotFoundException\n
        Allows for 'my_data = some_bucket[key]' syntax'''
        return self._loopdy_loop(key, state="find")

    def __len__(self):
        ''' length_of_structure = len(some_bucket) '''
        return self.size
