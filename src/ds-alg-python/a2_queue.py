class Queue(object):
    """docstring for Queue."""
    #Constructor creates a list.
    def __init__(self):
        super(Queue, self).__init__()
        self.queue = list()

    # Adding elements to queue.
    def enqueue(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return

    # Removing the last element from the queue (the one entered first).
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ('Queue Empty!')

    def size(self):
        return len(self.queue)

    # Display the elements of the queue.
    def display_queue(self):
        return self.queue




def main():
    print("python3: implement Queue Data Structure.")

    myQueue = Queue()
    print(myQueue.enqueue('Muhammad'))
    print(myQueue.enqueue('Hafidz'))
    print(myQueue.enqueue('Inma'))
    print(myQueue.enqueue('Reyes'))
    print(myQueue.enqueue('Guerrera'))
    print('the queue now = ', myQueue.display_queue())
    print('the size of queue now = ', myQueue.size())
    print('the longest string of queue now = ', max(myQueue.display_queue(), key=len))
    print('remove one element', myQueue.dequeue())
    print('the queue now = ', myQueue.display_queue())
    print('the size of queue now = ', myQueue.size())

if __name__ == '__main__':
    main()
