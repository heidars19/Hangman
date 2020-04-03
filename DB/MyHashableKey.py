
class MyHashableKey():
    def __init__(self, integer, key_string):
        self.num = integer
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
