class Node(object):
    """docstring for Node."""


    # A Python class that represents an individual node
    # in a Binary Tree.
    # Initialise nodes.
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.left = None
        self.right = None

    # Inset data element to the node.
    def insert_data(self, data):
        # Compare the new value with the parent node.
        if self.data:
            if data < self.data:
                if self.left is None:
                    # If left node is empty.
                    # Create a new node for the left.
                    self.left = Node(data)
                else:
                    # Insert a new data to the left.
                    self.left.insert_data(data)
            elif data > self.data:
                if self.right is None:
                    # If right node is empty.
                    # Create a new node for the right.
                    self.right = Node(data)
                else:
                    # Insert a new data to the right.
                    self.right.insert_data(data)
        else:
            self.data = data

    # Print data elements of the nodes.
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print('node = {0}'.format(self.data))
        if self.right:
            self.right.print_tree()

    # In-order traversal.
    # Left -> Root -> Right.
    def inorderTraversal(self, rootData):
        visitNodes = []
        if rootData:
            visitNodes = self.inorderTraversal(rootData.left)
            visitNodes.append(rootData.data)
            print('current node(s) => ',format(visitNodes))
            visitNodes = visitNodes + self.inorderTraversal(rootData.right)
        return visitNodes



def main():
    print(end='\n')
    print("python3: implement Binary Tree Data Structure.")

    rootNode = Node(12)
    rootNode.insert_data(6)
    rootNode.insert_data(14)
    rootNode.insert_data(2)
    rootNode.insert_data(50)
    rootNode.print_tree()

    print(end='\n')
    print("In-order Traversal:")
    print(rootNode.inorderTraversal(rootNode))

    print(end='\n')


if __name__ == '__main__':
    main()
