from DB.MyHashableKey import MyHashableKey
from DB.Errors import *
from DB.Bucket import Bucket


class HashMap():
    def __init__(self):
        self.size = 16
        self.list = [None for _ in range(self.size)]
        self.len = 0

    def __str__(self):
        ret_str = ""
        for i in range(self.size):
            if self.list[i] != None:
                ret_str += "index :" + str(i) + "\n" + str(self.list[i])
        return ret_str.strip()

    def __index(self, num, data_str):
        index = MyHashableKey(num, data_str)
        return hash(index)

    # def insert(self, key, data):
    def insert(self, key, data):
        '''Adds a key:value to the data structure. Creates a bucket if needed, or adds to an already existing one'''
        index = self.__index(self.size, key)
        # print("key: {}, index: {}, data: {}".format(key, index, data))
        if self.list[index] == None:
            # Creates a bucket if none exists
            self.list[index] = Bucket()
        # otherwise just adds to the current bucket
        self.list[index].insert(key, data)
        self.len += 1

    # def update(self, key, data):
    def update(self, key, data):
        '''Find indexed value, goes into bucket and updates it with new values.\n
        Raises NotFoundEcxeption if index not found or if key does not match a key in the bucket.'''
        index = self.__index(self.size, key)

        if self.list[index] != None:
            self.list[index].update(key, data)
        else:
            raise NotFoundException

    # def find(self, key):
    def find(self, key):
        ''' Accepts a key, returns corresponding value '''
        index = self.__index(self.size, key)

        if self.list[index] != None:
            return self.list[index].find(key)
        else:
            raise NotFoundException

    # def contains(self, key):
    def contains(self, key):
        ''' Returns True of False depending on wether Key exists or not. '''
        index = self.__index(self.size, key)

        if self.list[index] != None:
            return self.list[index].contains(key)
        else:
            return False

    # def remove(self, key):
    def remove(self, key):
        ''' Remove a key and it's value from a bucket.\n
        If it was the last value in the bucket, it also removes the pointer to that bucket.\n
        Raises NotFoundException if Key isn't found.'''
        index = self.__index(self.size, key)

        if self.list[index] != None:
            self.list[index].remove(key)
            self.len -= 1
            if self.list[index].size == 0:
                self.list[index] = None
        else:
            return NotFoundException

    # def __setitem__(self, key, data):
    def __setitem__(self, key, data):
        ''' Inserts a new key/value pair, updates an existing value if key already exists. '''
        index = self.__index(self.size, key)

        if self.list[index] != None:
            if self.list[index].contains(key):
                # If key exists, we update
                self.list[index].update(key, data)
            else:
                # If key doesn't exist, we insert a new key/value pair
                self.list[index][key] = data
                self.len += 1
        else:
            self.insert(key, data)
            self.len += 1

    # def __getitem__(self, key):
    def __getitem__(self, key):
        index = self.__index(self.size, key)

        if self.list[index] != None:
            if self.list[index].contains(key):
                return self.list[index][key]
            else:
                return None
        else:
            return None

    # def __len__(self):
    def __len__(self):
        return self.len
