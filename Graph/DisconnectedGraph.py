'''
You are given a graph with 𝑁 vertices (numbered from 1 to 𝑁) and 𝑀 bidirectional edges. Two vertices are considered “directly connected” if there is an edge between them, while they are deemed “connected” if there is a path between them. Conversely, two vertices are considered “disconnected” if there is no path connecting them.

You are allowed to perform an operation where you can shift an edge between two directly connected vertices to connect a pair of currently disconnected vertices. Your task is to determine the minimum number of operations required to make the entire graph connected. If it is impossible to achieve connectivity, return -1.

 **Note**:

A connected graph is a graph that is connected in the sense of a topological space, i.e., there is a path from any vertex to any other vertex in the graph.

There are no repeated edges and self-loops in the graph.



**Example**:

Let’s say ‘N’ is 4 and ‘M' is 3. The 3 edges are (1,2), (2,3) and (1,3). Then our graph will look as follows:-





To make the graph connected we can shift the edge between (1,3) to (1,4). This operation will make the graph connected.

There are multiple ways in which we can make the above graph connected. However, minimum 1 operation is required.

Input Format:

The first line contains a single integer ‘T’ representing the number of test cases.

The first line of each test case contains two space-separated integers ‘N’ and ‘M’ representing the number of vertices and the number of edges in the graph.

Each of the next ‘M’ lines contains two space-separated integers representing the vertices that are directly connected by an edge.

Constraints:

1 <= T <= 10

1 <= N <= 10000

1 <= M <= 10000

1 <= U[i], V[i] <= N

Where ‘T’ is the number of test cases.‘N’ is the number of vertices in the graph. ‘M’ is the number of edges in the graph. ‘U[i]’ and ‘V[i]’ are vertices of the i-th edge.

 You should do this question in O(N+M) time complexity, where N is the total number of vertices and M is the total number of edges.

Output:

For each test case, print a single line containing a single integer denoting the minimum number of operations to make the graph connected. If it is not possible to make a graph connected print -1.

The output of each test case will be printed in a separate line.

Sample Input 1:
2

4 3

1 2

2 3

3 1

4 3

1 2

2 3

3 4

Sample Output 1:

1

0
'''
class DisconnectedGraph:

    def __init__(self):
        self.redundant_edges = 0
        self.adj_list = [[]]
        self.visited = []
        self.components = 0

    # DFS to find connected components
    def depth_first_search(self,node):
        stack = [node]
        self.visited[node] = True
        size = 0  # Size of the component
        while stack:
            current = stack.pop()
            size += 1
            for neighbor in self.adj_list[current]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    stack.append(neighbor)
                else:
                    if stack:
                        self.redundant_edges += 1

        return size

    def findNodeAndRedundantEdges(self,n, edges):
        # Initialize the adjacency list for the graph
        self.adj_list = [[] for _ in range(n + 1)]

        # Create the graph from the edge list
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

        # To track visited vertices and number of components
        self.visited = [False] * (n + 1)
        self.components = 0
        self.redundant_edges = 0

        # Run DFS from every unvisited node
        for i in range(1, n + 1):
            if not self.visited[i]:
                self.components += 1
                self.depth_first_search(i)

        # Redundant edges are counted twice due to the bidirectional nature of the graph.
        self.redundant_edges //= 2

        return self.components, self.redundant_edges

    def MinOperationsToConnect(self,n, m, edges):
        components, redundant_edges = self.findNodeAndRedundantEdges(n, edges)

        # If there are C components, we need C-1 edges to connect them
        if components == 1:
            return 0
        elif redundant_edges >= components - 1:
            return components - 1
        else:
            return -1

if __name__ == '__main__':
    graph = DisconnectedGraph()

    t = int(input())  # Number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # Number of vertices and edges
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        print(graph.MinOperationsToConnect(n, m, edges))
