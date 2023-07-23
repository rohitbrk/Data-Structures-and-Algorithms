class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            itr = self.head
            while itr.next != self.head:
                itr = itr.next
            itr.next = node
            node.next = self.head

    def print(self):
        if self.head is None:
            print("cicular linked list is empty")
            return

        itr = self.head
        s = ""
        while itr:
            s += str(itr.data)+"-->"
            if itr.next == self.head:
                break
            itr = itr.next

        print(s)


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_end(1)
    cll.insert_at_end(2)
    cll.insert_at_end(3)
    cll.print()
