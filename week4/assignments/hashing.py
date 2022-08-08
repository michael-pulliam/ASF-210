
class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self, key):
        keystr = str(key)
        hashVal = 0
        for ch in keystr:
            hashVal += ord(ch)
        
        return (hashVal*len(keystr)) % self.size
        # return hashVal % self.size # Modulo Operator
        
    def rehashFunction(self, key):
        # Insert your secondary hashing function code
        keystr = str(key)
        hashVal = 0
        counter = 0
        for ch in keystr:
            counter += 1
            hashVal += ord(ch)+counter
        
        return (hashVal*len(keystr)) % self.size
        # return hashVal % self.size # Modulo Operator


    def put(self,key,data):
        # Insert your code here to store key and data    
        h = self.hashFunction(key)
        
        while self.slots[h] and self.data[h]:
            h = self.rehashFunction(key) 
            break 
        self.data[h] = data
        self.slots[h] = key
            


    def get(self,key):
        # Insert your code here to get data by key
        return self.data[self.hashFunction(key)]

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'
H.put(66, 'B')
H.put(80, 'C')
H.put(35, 'D')
H.put(18, 'E')
H.put(52, 'F')
H.put(89, 'G')
H.put(70, 'H')
H.put(12, 'I')
# Store remaining input data

# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H.get(52))

