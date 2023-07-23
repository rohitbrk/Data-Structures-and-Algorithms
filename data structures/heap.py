import heapq


class Heap:
    def __init__(self, array):
        heapq.heapify(array)
        self.array = list(array)


if __name__ == "__main__":
    array = [29, 35, 1, 3, 89]
    heap = Heap(array)
    print("heap: ", heap.array)
