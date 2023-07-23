class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def printLinkedList(head):
    while True:
        print(str(head.data) + "->")
        if not head.next:
            break
        head = head.next


if __name__ == "__main__":
    el5 = Node(5, None)
    el4 = Node(4, el5)
    el3 = Node(3, el4)
    el2 = Node(2, el3)
    el1 = Node(1, el2)

    printLinkedList(el1)
