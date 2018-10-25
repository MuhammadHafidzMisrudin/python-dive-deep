class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval) # Add element to top of stack.
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return ('No Element in the Stack')
        self.stack.pop() # Remove element from top of stack.

    def peek(self):
        # Get the value of the top element without removing it.
        if self.stack == []:
            raise Exception('Stack Empty!')
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

    def display_stack(self):
        return self.stack


def main():
    print("python3: implement Stack Data Structure.")

    myStack = Stack()
    myStack.add('Muhammad')
    myStack.add('Inma')
    myStack.add('Reyes')
    myStack.add('Guerrera')
    print('all elements in a stack = ', myStack.display_stack())
    print('peek stack now, ', myStack.peek())
    print('remove an element on the top of stack now, ', myStack.remove())
    print('all elements in a stack = ', myStack.display_stack())
    print('peek stack now, ', myStack.peek())
    print('remove an element 1th on the top of stack now, ', myStack.remove())
    print('remove an element 0th on the top of stack now, ', myStack.remove())
    print('all elements in a stack = ', myStack.display_stack())
    print('peek stack now, ', myStack.peek())
    myStack.add('Inma')
    myStack.add('Hafidz')
    print('all elements in a stack = ', myStack.display_stack())


if __name__ == '__main__':
    main()
