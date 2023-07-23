class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)

        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


if __name__ == "__main__":
    ht1 = HashTable()
    ht1["march 6"] = 10
    ht1["march 17"] = 100
    print(ht1.get_hash("march 6"), ht1.get_hash("march 17"))
    print(ht1.arr)

# class HashTable:
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [None for i in range(self.MAX)]

#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX

#     def __getitem__(self, index):
#         h = self.get_hash(index)
#         return self.arr[h]

#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         self.arr[h] = val


# t = HashTable()
# t["march 6"] = 1
# t["march 17"] = 2
# print(t["march 6"],
#       t["march 17"])
