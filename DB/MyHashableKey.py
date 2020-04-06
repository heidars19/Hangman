
class MyHashableKey():
    ''' Accepts intereg and a string.\n
    Integer is the length of spread for the index,\n
    String will be used for hash. '''

    def __init__(self, integer_value, key_string):
        self.num = integer_value
        self.skey = str(key_string)

    def __str__(self):
        return self.skey + " " + str(self.num)

    def __hash__(self):
        num = 1
        for i in range(len(self.skey)):
            num += ord(self.skey[i])*13
        return (num * 17) % self.num

    def __eq__(self, other):
        return hash(self) == hash(other)


if __name__ == "__main__":
    myhash = MyHashableKey(16, "þúsundblaðarós")
    print(hash(myhash))
