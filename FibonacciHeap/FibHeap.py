'''
Starting with an empty heap, you have to perform the Insertion, Deletion and Replace operations on the fibonacci heap and print the number of root nodes in the resultant structure.

Note:

The maximum number of childs for any node will not exceed 4

Input Format:

Here the first line contains the total number of operations N. Here, Operations can be of 3 types

I 10   - Insert 10

D      - Delete Min

R 10 1 - Replace the value of 10 with 1.

So the next N lines will be one of the above three types.

Constraints:

Number of Child for any Node <= 4

Maximum Number of min heaps in a Fibonacci Heap <= 50

Output Format:
Print the number of root nodes in a fibonacci heap, after performing all the operations in the same order as input.

Sample Input 1:

11

I 10

I 20

I 30

I 40

I 50

I 60

D

I 70

R 40 35

R 35 15

D

Sample Output 1:

2
'''


from tempfile import tempdir
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self
        self.right = self
        self.parent = None
        self.child = None
        self.degree = 0
        self.mark = False


class FibHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0
        self.root_list = None


    def insert(self, value):
        #new_node = Node(value)
        n =  Node(value)
        n.left = n.right = n
        self.merge_with_root_list(n)
        if self.min_node is None or n.value < self.min_node.value:
            self.min_node = n
        self.total_nodes += 1

    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node

    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child is not None:
                # attach child nodes to root list
                children = [x for x in self.iterate(z.child)]
                for i in range(0, len(children)):
                    self.merge_with_root_list(children[i])
                    children[i].parent = None
            self.remove_from_root_list(z)
            # set new min node in heap
            if z == z.right:
                self.min_node = self.root_list = None
            else:
                self.min_node = z.right
                self.consolidate()
            self.total_nodes -= 1
        return z

    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    def consolidate(self):
        A = [None] * 4
        nodes = [w for w in self.iterate(self.root_list)]
        for w in range(0, len(nodes)):
            x = nodes[w]
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.value > y.value:
                    temp = x
                    x, y = y, temp
                self.heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        # find new min node - no need to reconstruct new root list below
        # because root list was iteratively changing as we were moving
        # nodes around in the above loop
        for i in range(0, len(A)):
            if A[i] is not None:
                if A[i].value < self.min_node.value:
                    self.min_node = A[i]

    def heap_link(self, y, x):
        self.remove_from_root_list(y)
        y.left = y.right = y
        self.merge_with_child_list(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False

    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    def replace_key(self, old_value, new_value):
        node = self.search_node(old_value)
        if node is not None:
            node.value = new_value


    def cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def cut(self, x, y):
        self.remove_from_child_list(y, x)
        y.degree -= 1
        self.merge_with_root_list(x)
        x.parent = None
        x.mark = False

    def remove_from_child_list(self, parent, node):
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left

    def count_roots(self):
        node = stop = self.root_list
        count = 0
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            node = node.right
            if node.value != node.right.value:
                count = count+1
        print(count)

    def search_node(self, value):
        start = self.min_node
        if start is None:
            return None
        # Use a queue to traverse nodes in the circular doubly linked list
        queue = [start]
        visited = set()

        while queue:
            node = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            if node.value == value:
                return node
            if node.child is not None:
                queue.append(node.child)
            # Traverse siblings
            sibling = node.right
            while sibling != node:
                if sibling not in visited:
                    queue.append(sibling)
                sibling = sibling.right
        return None

if __name__ == '__main__':
    n = int(input())  # Number of operations
    fib_heap = FibHeap()

    for _ in range(n):
        operation = input().split()
        if operation[0] == 'I':
            value = int(operation[1])
            fib_heap.insert(value)
        elif operation[0] == 'D':
            fib_heap.extract_min()
        elif operation[0] == 'R':
            old_val = int(operation[1])
            new_val = int(operation[2])
            fib_heap.replace_key(old_val, new_val)

    # Output the number of root nodes
    fib_heap.count_roots()
