class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self, index):
        return self.stack[index]


def main():
    print("python3: implement Stack Data Structure.")

    myStack = Stack()
    myStack.add('Muhammad')
    myStack.add('Inma')
    print(myStack.stack)
    print(myStack.peek(1))


if __name__ == '__main__':
    main()
