class Array:
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def find(self, index):
        return self.array[index]

    def insert(self, index, item):
        self.array[index] = item

    def delete_by_index(self, index):
        self.array[index] = None

    def get_index(self, item):
        for i, val in enumerate(self.array):
            if val == item:
                return i

    def delete_by_item(self, item):
        index = self.get_index(item)
        self.delete_by_index(index)

    def __str__(self):
        return str(self.array)


if __name__ == "__main__":
    array1 = Array()
    array1.add(1)
    array1.add(2)
    array1.add(3)
    print(array1)
    item_at_index_1 = array1.find(1)
    print(item_at_index_1)
    array1.insert(0, 100)
    print(array1)
    array1.delete_by_index(2)
    print(array1)
    array1.delete_by_item(100)
    print(array1)
