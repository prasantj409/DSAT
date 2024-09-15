class MaxHeap:
    def __init__(self):
        self.heap = [100, 230, 44, 1, 74, 12013, 84]
        self.max_size = 7
        self.heap_size = 7


    def lchild(self, index) :
        return 2*index +1

    def rchild(self,index):
        return 2*index+2

    def swap(self,index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def heapify(self, i):
        largest = i
        l = self.lchild(largest)
        r = self.rchild(i)
        if l < self.heap_size and self.heap[self.lchild(largest)] > self.heap[i]:
            largest = l

        if r < self.heap_size and self.heap[self.rchild(i)] > self.heap[largest]:
            largest = r

        if largest != i:
            self.swap(i,largest)
            self.heapify(largest)

    def MinHeapify(self, i):
        lowest = i
        l = self.lchild(lowest)
        r = self.rchild(i)
        if l < self.heap_size and self.heap[l] < self.heap[i]:
            lowest = l

        if r < self.heap_size and self.heap[r] < self.heap[lowest]:
            lowest = r

        if lowest != i:
            self.swap(i,lowest)
            self.heapify(lowest)

if __name__ == '__main__':
    maxHeap = MaxHeap()
    n = int((maxHeap.heap_size - 1) // 2) -1
    for j in range(n,-1,-1):
        maxHeap.heapify(j)


    for val in maxHeap.heap:
        print(val)