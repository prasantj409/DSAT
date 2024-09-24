"""
Imagine a magical carriage that needs to travel through an enchanted forest to reach a distant castle. The journey is measured in fairy miles, and there are special wells along the way where the carriage can collect fairy dust to keep going.

Each well is described by a list with two numbers: where the well is located (in fairy miles) and how much fairy dust it has. The carriage starts with a certain amount of fairy dust and uses one unit of dust for each mile traveled.

There is no limit to the quantity of fairy dust that the magical carriage can collect at any instant.

Your task is to figure out the minimum number of times the carriage needs to stop at these wells to reach the castle. If it’s not possible to reach the castle, return -1.

Note that the carriage can still stop at a well even if it just reaches there by exhausting all the fairy dust. Also the carriage will be considered to have reached its destination if it arrives there with 0 dust remaining.

Input: The first line contains  the distance to the destination in fairy miles. The next line contains the initial fairy dust. And the last line contains the list of wells, where each entry represents its location and the magical dust it can provide. The wells are arranged in sorted order as per their location. The number of wells can be between 0 to 500 (inclusive).

Output: Print the minimum number of stops to reach the destination and -1 if it’s not possible.

Solve this question using Heaps and no inbuilt function for the same is allowed. Else 0 marks will be awarded for the whole assignment.

Sample Input:

34

5

[[5,10], [10, 6], [12, 100]]

Sample Output

2

Explanation: First stop at [5,10] and next stop at [12, 100]


"""

import ast


class FairyMiles:
    def __init__(self):
        self.heap = [0 for x in range(1000)]
        self.max_size = 7
        self.heap_size = 0

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
        if l <= self.heap_size and self.heap[self.lchild(largest)] > self.heap[i]:
            largest = l

        if r <= self.heap_size and self.heap[self.rchild(i)] > self.heap[largest]:
            largest = r

        if largest != i:
            self.swap(i,largest)
            self.heapify(largest)

    def insert(self,data):
        self.heap[self.heap_size] = data
        if self.heap_size > 0:
            self.heapifyData()

        self.heap_size = self.heap_size + 1

    def heapifyData(self):
        n = int((self.heap_size + 1) // 2) - 1
        for j in range(n, -1, -1):
            self.heapify(j)

    def extract_max(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size = self.heap_size -1
        if self.heap_size > 0:
            self.heapify(0)
        return popped

if __name__ == '__main__':
    fairyMiles = FairyMiles()

    total_distance = int(input())
    fuel = int(input())
    wells = input()
    if wells == "":
        wells="[]"
    current_fuel = fuel
    current_location = 0
    stops = 0
    well_list = ast.literal_eval(wells)
    if len(well_list) == 0:
        print("-1")
    else:
        well_list.append([total_distance, 0])
        for location, fuel in well_list:
            distance_needed = location - current_location

            current_fuel = current_fuel - distance_needed
            while current_fuel < 0 and fairyMiles.heap_size >= 0:
                current_fuel = current_fuel + fairyMiles.extract_max()
                stops +=1

            if current_fuel < 0:
                print("-1")
            fairyMiles.insert(fuel)
            current_location = location

        print(stops)

