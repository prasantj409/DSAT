class BNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Binary Search Tree Operations
class BST:
    def insert(self,data, root):
        if root is None:
            return BNode(data)

        if data < root.data:
            root.left = self.insert(data,root.left)
        else:
            root.right = self.insert(data, root.right)

        return root

    def traversePreOrder(self,root):
        if root is not None:
            self.visitNode(root)
            self.traversePreOrder(root.left)
            self.traversePreOrder(root.right)

    def visitNode(self,root):
        print(root.data)

    def traverseInOrder(self,root):
        if root is not None:
            self.traversePreOrder(root.left)
            self.visitNode(root)
            self.traversePreOrder(root.right)

if __name__ == '__main__':
    bst = BST()
    node = BNode(6)
    bst.insert(1,node)
    bst.insert(2, node)
    bst.insert(3, node)
    bst.insert(4, node)
    bst.traversePreOrder(node)
    bst.traverseInOrder(node)