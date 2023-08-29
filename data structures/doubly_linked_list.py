class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_b(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)

        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print(self):
        if self.length() == 0:
            print("DLinked List is empty")

        itr = self.head
        dllstr = ""
        while itr:
            dllstr += str(itr.data)+"-->"
            itr = itr.next

        print(dllstr)


if __name__ == "__main__":
    dll = DLinkedList()
    print("Length:", dll.length())
    dll.print()
    dll.insert_at_b(3)
    dll.insert_at_b(2)
    dll.insert_at_b(1)
    dll.print()
    print("Length:", dll.length())
