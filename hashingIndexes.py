class HashTable:

    dbKeyMaping = dict()


    def addEntry(self, key, value):
        self.dbKeyMaping[key] = value

    def updateValue(self, key, value):
        self.dbKeyMaping[key] = value

    def deleteEntry(self, key):
        self.dbKeyMaping.pop(key)
        

    def traverse(self):
        for key, value in self.dbKeyMaping.items():
            print(key, " : ", value)


    def printKeys(self):
        print("keys")
        for key in self.dbKeyMaping.keys():
            print("   " ,key)


    def printValues(self):
        print("values")
        for value in self.dbKeyMaping.values():
            print("   ",value)


ht = HashTable()
ht.addEntry(1, 101)
ht.addEntry(2, 202)
ht.addEntry(3, 303)
ht.traverse()
ht.printKeys()
ht.printValues()

