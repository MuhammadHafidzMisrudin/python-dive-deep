class Node(object):
    """docstring for Node."""

    # Constructor creates a Node.
    def __init__(self, dataVal, nextNode=None):
        super(Node, self).__init__()
        self.dataVal = dataVal
        self.nextNode = nextNode

class SingleLinkedList(object):
    """docstring for SingleLinkedList."""

    # Constructor creates a Linked List.
    def __init__(self, headVal=None):
        super(SingleLinkedList, self).__init__()
        self.headVal = headVal
        self.size = 0

    # Traversing a Linked List and Print List.
    def print_linked_list(self):

        # Initialise a node.
        eachNode = self.headVal

        # Loop through each node in a list if not empty.
        while eachNode is not None:
            print(eachNode.dataVal)
            eachNode = eachNode.nextNode



def main():
    print("python3: implement LinkedList Data Structure.")

    # Create a Linked List object.
    myLinkedList = SingleLinkedList()

    # Create a first node element as head.
    myLinkedList.headVal = Node('Inma')

    # Create a second node element.
    elVal2 = Node('Muhammad')

    # Create a third node element.
    elVal3 = Node('Hafidz')

    # Link head (first node element) to second node element.
    myLinkedList.headVal.nextNode = elVal2

    # Link second node element to third node element.
    elVal2.nextNode = elVal3

    # Print out a Linked List.
    myLinkedList.print_linked_list()


if __name__ == '__main__':
    main()
