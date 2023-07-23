class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_b(self, data):
        self.head = Node(data, self.head)

    def insert_at_e(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert(self, values):
        for value in values:
            self.insert_at_e(value)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            print("Invalid index")

        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.length():
            print("Invalid index")

        if index == 0:
            self.insert_at_b(data)

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data, itr.next)
                itr.next = node
                return

            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return

            itr = itr.next

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data)+"-->"
            itr = itr.next

        print(llstr)


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert_at_b(1)
    ll1.insert_at_b(2)
    ll1.insert_at_b(3)
    ll1.insert_at_e(4)
    ll1.insert_at_e(5)
    ll1.insert_at_e(6)
    ll1.insert([7])
    ll1.insert([8, 9])
    print("Length:", ll1.length())
    ll1.print()
    ll1.remove_at(2)
    ll1.print()
    ll1.insert_at(2, 100)
    ll1.print()
    ll1.insert_after_value(100, 200)
    ll1.print()
    ll1.remove_by_value(5)
    ll1.print()
