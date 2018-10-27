class Node(object):
    """docstring for Node."""
    def __init__(self, dataVal, nextNode=None):
        super(Node, self).__init__()
        self.dataVal = dataVal
        self.nextNode = nextNode

class SingleLinkedList(object):
    """docstring for SingleLinkedList."""
    def __init__(self, headVal=None):
        super(SingleLinkedList, self).__init__()
        self.headVal = headVal
        self.size = 0


def main():
    print("python3: implement LinkedList Data Structure.")

    myLinkedList = SingleLinkedList()


if __name__ == '__main__':
    main()
