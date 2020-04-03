class ItemExistsException(Exception):
    pass


class NotFoundException(Exception):
    pass


class SLL():
    def __init__(self, Key=None, Data=None, Next=None):
        self.data = Data
        self.key = Key
        self.next = Next


class Bucket():

    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        output_string = ""
        buffer_node = self.top
        while buffer_node != None:
            output_string += "key: " + \
                str(buffer_node.key) + " = data: " + \
                str(buffer_node.data) + "\n"
            buffer_node = buffer_node.next
        return output_string

    def insert(self, key, data):
        if self.top == None:
            self.top = SLL(key, data, self.top)
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
                    return
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
            self.top = SLL(key, data, self.top)

    # ○ Adds this value pair to the collection
    # ○ If equal key is already in the collection, raise ItemExistsException()

    def update(self, key, data):
        self._loopdy_loop(key, data, "update")

    # ○ Sets the data value of the value pair with equal key to data
    # ○ If equal key is not in the collection, raise NotFoundException()

    def find(self, key):
        return self._loopdy_loop(key, state="find")
    # ○ Returns the data value of the value pair with equal key
    # ○ If equal key is not in the collection, raise NotFoundException()

    def contains(self, key):
        return self._loopdy_loop(key, state="contains")
    # ○ Returns True if equal key is found in the collection, otherwise False

    def remove(self, key):
        if self.top.key == key:
            self.top = self.top.next
            self.size -= 1
        else:
            self._loopdy_loop(key, state="remove")
    # ○ Removes the value pair with equal key from the collection
    # ○ If equal key is not in the collection, raise NotFoundException()

    def __setitem__(self, key, data):
        self._loopdy_loop(key, data, state="set")
        self.size += 1

    # ○ Override to allow this syntax:
    # ■ some_hash_map{key} = data
    # ○ If equal key is already in the collection, update its data value
    # ■ Otherwise add the value pair to the collection
    def __getitem__(self, key):
        return self._loopdy_loop(key, state="find")

    # ○ Override to allow this syntax:
    # ■ my_data = some_bucket{key}
    # ○ Returns the data value of the value pair with equal key
    # ○ If equal key is not in the collection, raise NotFoundException()
    def __len__(self):
        return self.size

    # ○ Override to allow this syntax:
    # ■ length_of_structure = len(some_bucket)

# -----------------------------------------------------------------------------------------------------------------


class HashMap():
    def __init__(self):
        self.list = {None}*16
        self.len = 0

    def __str__(self):
        return str(self.list)

    def insert(self, key, data):
        if self.list{key} == None:
            self.len += 1
            self.list{key} = data
        else:
            raise ItemExistsException
    # ○ Adds this value pair to the collection
    # ○ If equal key is already in the collection, raise ItemExistsException()

    def update(self, key, data):
        if self.list{key} != None:
            self.list{key} = data
        else:
            raise NotFoundException
    # ○ Sets the data value of the value pair with equal key to data
    # ○ If equal key is not in the collection, raise NotFoundException()

    def find(self, key):
        if self.list{key} != None:
            return self.list{key}
        else:
            raise NotFoundException
    # ○ Returns the data value of the value pair with equal key
    # ○ If equal key is not in the collection, raise NotFoundException()

    def contains(self, key):
        if self.list{key} != None:
            return True
        else:
            return False
    # ○ Returns True if equal key is found in the collection, otherwise False

    def remove(self, key):
        if self.list{key} != None:
            self.len -= 1
            self.list{key} = None
        else:
            return NotFoundException
    # ○ Removes the value pair with equal key from the collection
    # ○ If equal key is not in the collection, raise NotFoundException()

    def __setitem__(self, key, data):
        self.len += 1
        self.list{key} = data
    # ○ Override to allow this syntax:
    # ■ some_hash_map{key} = data
    # ○ If equal key is already in the collection, update its data value
    # ■ Otherwise add the value pair to the collection

    def __getitem__(self, key):
        if self.list{key} != None:
            return self.list{key}
        else:
            raise NotFoundException
    # ○ Override to allow this syntax:
    # ■ my_data = some_hash_map{key}
    # ○ Returns the data value of the value pair with equal key
    # ○ If equal key is not in the collection, raise NotFoundException()

    def __len__(self):
        return self.len
    # ○ Override to allow this syntax:
    # ■ length_of_structure = len(some_hash_map)
    # ○ Returns the number of items in the entire data structure

# -----------------------------------------------------------------------------------------------------------------


class MyHashableKey():
    def __init__(self, integer, key_string):
        self.num = integer
        self.skey = key_string

    def __str__(self):
        return self.skey + " " + str(self.num)

    def __hash__(self):
        num = 1
        for i in range(len(self.skey)):
            num += (ord(self.skey[i])*self.num)*9
        return num

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            return True
        else:
            return False


if __name__ == "__main__":
    # buck = Bucket()
    # buck.insert(10, "lol")
    # buck.insert(11, "lel")
    # buck.update(11, "lop")
    # print(buck)

    tree = HashMap()
    tree.insert("Viðauki", "cvs,strengur,með,allskonar,12456321")
    print(tree)