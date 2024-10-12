'''
You are given a network of n cities connected by Indian railways. The connections between cities are represented as an array of trains, where each element trains[i] = [A, B, C] indicates that there is a train from city A to city B with a travel cost of C. The connections are bidirectional.

Your task is to find the lowest-cost route from a specified starting city to a destination city, subject to the constraint of making at most m stops along the way. If such a route does not exist, you should return -1.

Input Format:

First line contains an integer n which denotes the number of cities (starting from 0 to n-1).

Second line contains an array of trains which contains [fromCity, toCity, cost]

Third line contains the starting city.

Fourth line contains the destination city.

Fifth line contains the maximum number of stops m. (starting and ending nodes are not included)

Constraints:

1 <= n <= 100

0 <= trains.length <= (n * (n - 1) / 2)

Note: Your algorithm must run in O(n+e.m) time complexity, where n is number of cities, e is number of trains and m is number of stops



Output Format:

Output a single integer, which denotes the least price path from start to end.

Sample Input 1

7

[[1, 2, 20], [1, 3, 10], [1, 6, 30], [2, 5, 40], [3, 4, 50], [4, 5, 60], [5, 6, 70], [0, 1, 22]]

0

6

12

Sample Output 1
52
'''

import heapq
class MinCost:
    def __init__(self, destination, max_stops):
        self.queue = []
        self.destination = destination
        self.max_stops = max_stops

    def calculateCost(self, graph ):
        min_cost = {}
        while self.queue:
            current_cost, current_city, stops = heapq.heappop(self.queue)
            if current_city == self.destination and stops <= self.max_stops:
                return current_cost
            if stops > self.max_stops:
                continue

            for neighbor, cost in graph[current_city]:
                new_cost = current_cost + cost
                new_stops = stops + 1

                if new_stops <= self.max_stops and (neighbor, new_stops) not in min_cost or new_cost < min_cost.get(
                        (neighbor, new_stops), float('inf')):
                    min_cost[(neighbor, new_stops)] = new_cost
                    heapq.heappush(self.queue, (new_cost, neighbor, new_stops))

        return -1

    def FindLeastCost(self, cities, trains, start):
        # Build the adjacency list
        graph = {i: [] for i in range(cities)}
        for train in trains:
            from_city, to_city, cost = train
            graph[from_city].append((to_city, cost))

        self.queue = [(0, start, -1)]
        return self.calculateCost(graph)

if __name__ == '__main__':
    cities = int(input())  # Number of cities
    trains = eval(input())  # Train routes
    start = int(input())  # Starting city
    destination = int(input())  # Destination city
    max_stops = int(input())  # Maximum stops allowed
    minCost = MinCost(destination, max_stops)

    result = minCost.FindLeastCost(cities, trains, start)
    print(result)

