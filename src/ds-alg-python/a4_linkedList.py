class Node(object):
    """docstring for Node."""

    # Constructor creates a Node.
    def __init__(self, dataVal=None):
        super(Node, self).__init__()
        self.dataVal = dataVal
        self.nextNode = None

class SingleLinkedList(object):
    """docstring for SingleLinkedList."""

    # Constructor creates a Linked List.
    def __init__(self, headVal=None):
        super(SingleLinkedList, self).__init__()
        self.headVal = headVal
        self.size = 0

    # Inserting at the Beginning of the Linked List.
    def add_node_at_beginning(self, newData):

        # Create a new node element.
        newNode = Node(newData)

        # Update the new nodes next val to existing node (head).
        newNode.nextNode = self.headVal
        self.headVal = newNode


    def get_size_linked_list(self):
        return self.size

    # Traversing a Linked List and Print List.
    def print_linked_list(self):

        # Initialise a node.
        eachNode = self.headVal

        # Loop through each node in a list if not empty.
        while eachNode is not None:
            print('node {0} = {1}'.format(eachNode, eachNode.dataVal))
            eachNode = eachNode.nextNode
            self.size += 1



def main():
    print(end='\n')
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

    myLinkedList.add_node_at_beginning('Baby')

    print('\n')
    # Print out a Linked List and its size.
    myLinkedList.print_linked_list()
    print('current size of LinkedList = {0}'.format(myLinkedList.get_size_linked_list()))


if __name__ == '__main__':
    main()
