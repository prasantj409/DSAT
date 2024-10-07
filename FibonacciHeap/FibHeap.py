from tempfile import tempdir


class node:
    def __init__(self, value):
        self.value = value
        self.left = self
        self.right = self
        self.parent = None
        self.child = None
        self.degree = 0

minHeapPtr = None
class FibHeap:



    def insert(self, value):
        new_node = node(value)
        global minHeapPtr
        if minHeapPtr is None:
            minHeapPtr = new_node
        else:
            # insert new node to the right of the min node. we have to preserve all connections
            #1. Set min node to the left of new node
            new_node.left = minHeapPtr
            # 2. set the original right of the min node to the right of new node as we are inserting new node between min node and its right node
            new_node.right = minHeapPtr.right
            #3. now, reconnect original right of min node to new node. we need to connect left of original right to new node
            minHeapPtr.right.left = new_node
            #4. now finally, connect new node to the right of min node
            minHeapPtr.right = new_node

            if new_node.value < minHeapPtr.value:
                minHeapPtr = new_node
