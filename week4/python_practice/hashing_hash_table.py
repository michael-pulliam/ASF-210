

# class HashItem:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

# class HashTable:
#     def __init__(self) -> None:
#         self.size = 256
#         self.slots = [None] * self.size
#         self.count = 0
        
#     def hashFunction(self, key):
#         keystr = str(key)
#         hashVal = 0
#         for ch in keystr:
#             hashVal += ord(ch)
        
#         return (hashVal*len(keystr)) % self.size
#         # return hashVal % self.size # Modulo Operator
        
#     def rehashFunction(self, key):
#         keystr = str(key)
#         hashVal = 0
#         counter = 0
#         for ch in keystr:
#             counter += 1
#             hashVal += ord(ch)+counter
        
#         return (hashVal*len(keystr)) % self.size
#         # return hashVal % self.size # Modulo Operator
    
#     def put(self, key, value):
#         # Store key:value pair
#         return
    
#     def get(self, key):
#         # Get value for key
#         return
    
# ht = HashTable()

# print(ht.hashFunction('John Smith'))
# print(ht.hashFunction('Jane Doe'))
# print(ht.hashFunction('George Washington'))
# print(ht.hashFunction('Mike Adams'))
# print(ht.hashFunction('Roberty Kohlbus'))
# print(ht.hashFunction('Alexander Hamilton'))
# print(ht.hashFunction(1234))
# print(ht.hashFunction(4321))
# print(ht.rehashFunction(4321))

# ----------------------------------------------------------------------------------------------------------------------------
# Hashing  -                             Python Data Structures and Algorithms by Benjamin Baka
# -----------------------------------------------------------------------------------------------------------------------------
class HashItem: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
print(sum(map(ord, 'hello world')))
    
class HashTable: 
    def __init__(self): 
        self.size = 256 
        self.slots = [None for i in range(self.size)] 
        self.count = 0 

    def _hash(self, key): 
        mult = 1 
        hv = 0 
        for ch in key: 
            hv += mult * ord(ch) 
            mult += 1 
        return hv % self.size 
    
    def put(self, key, value): 
        item = HashItem(key, value) 
        h = self._hash(key)
        
        while self.slots[h] is not None: 
            if self.slots[h].key is key: 
                break 
            h = (h + 1) % self.size
            
        if self.slots[h] is None: 
            self.count += 1 
        self.slots[h] = item
        
    def get(self, key): 
        h = self._hash(key)   

        while self.slots[h] is not None: 
            if self.slots[h].key is key: 
                return self.slots[h].value 
            h = (h+ 1) % self.size
            
    def __setitem__(self, key, value): 
        self.put(key, value) 

    def __getitem__(self, key): 
        return self.get(key)  

        return None

ht = HashTable() 
ht["good"] = "eggs" 
ht["better"] = "ham" 
ht["best"] = "spam" 
ht["ad"] = "do not" 
ht["ga"] = "collide" 

for key in ("good", "better", "best", "worst", "ad", "ga"): 
    v = ht[key] 
    print(v) 

print("The number of elements is: {}".format(ht.count)) 
    
# ht = HashTable() 
# ht.put("good", "eggs") 
# ht.put("better", "ham") 
# ht.put("best", "spam") 
# ht.put("ad", "do not") 
# ht.put("ga", "collide") 

# for key in ("good", "better", "best", "worst", "ad", "ga"): 
#     v = ht.get(key) 
#     print(v)                  
            
#-----------------------------------------------------------------------------------------------------------------------------
            

# ----------------------------------------------------------------------------------------------------------------------------
# Perfect Hashing Functions  -           Python Data Structures and Algorithms by Benjamin Baka
# -----------------------------------------------------------------------------------------------------------------------------


# def myhash(s): 
#     mult = 1 
#     hv = 0 
#     for ch in s: 
#         hv += mult * ord(ch) 
#         mult += 1 
#     return hv

# for item in ('hello world', 'world hello', 'gello xorld'): 
#     print("{}: {}".format(item, myhash(item))) 
    
    




# ----------------------------------------------------------------------------------------------------------------------------
# Symbol Table  -                         Python Data Structures and Algorithms by Benjamin Baka
# -----------------------------------------------------------------------------------------------------------------------------

name = "Joe" 
age = 27 