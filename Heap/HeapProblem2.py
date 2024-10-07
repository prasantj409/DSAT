"""
Given a list of N 3D points, your task is to determine the K closes points to the origin. Each points is represented as [x,y,z] and the distance from origin is calculated as per euclidean distance.

Input: The first line contains the number of 3D points: N. The next line contains the integer K and the last line contains the list of 3D points.

Output: Print the K closest points to the origin in the increasing order of their distance.

Solve this question using Heaps and no inbuilt function is allowed for the same. Else 0 marks will be awarded for the whole assignment.

Sample Input:
3

2

[[-6, -9, -4], [6, -2, 0], [-5, -4, 2]]

Sample Output

[[6, -2, 0], [-5, -4, 2]]
"""
import ast

class HeapProblem2:
    def __init__(self,n):
        self.heap = [0 for x in range(n+1)]
        self.heap_size = 0

    def lchild(self, index):
        return 2 * index + 1

    def rchild(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def heapify(self, i):
        largest = i
        l = self.lchild(largest)
        r = self.rchild(i)
        if l <= self.heap_size and self.heap[self.lchild(largest)][0] > self.heap[i][0]:
            largest = l

        if r <= self.heap_size and self.heap[self.rchild(i)][0] > self.heap[largest][0]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)

    def insert(self, distance, point):
        self.heap[self.heap_size] = [distance, point]
        if self.heap_size > 0:
            self.heapifyData()

        self.heap_size = self.heap_size + 1

    def heapifyData(self):
        n = ((self.heap_size + 1) // 2) - 1
        for j in range(n, -1, -1):
            self.heapify(j)

    def extract_max(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        if self.heap_size > 0:
            self.heapify(0)
        return popped

    def euclidean_distance(self,point):
        x, y, z = point
        return x**2 + y**2 + z**2

if __name__ == '__main__':


    N = int(input())
    K = int(input())
    points = input()
    originPoints = HeapProblem2(N)
    point_list = ast.literal_eval(points)

    for point in point_list:
        distance = originPoints.euclidean_distance(point)



        if K <= originPoints.heap_size:
            if originPoints.heap[0][0] > distance:
                originPoints.extract_max()
                originPoints.insert(distance, point)
        else:
            originPoints.insert(distance, point)


    list = []
    for j in range(originPoints.heap_size) :
        list.append(originPoints.heap[j])

    result = [item[1] for item in list]
    result.sort(key=originPoints.euclidean_distance)
    print(result)

