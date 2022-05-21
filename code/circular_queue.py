# This is the CircularQueue class
class CircularQueue:

    # constructor for the class
    # taking input for the size of the Circular queue
    # from user
    def __init__(self, maxSize):
        self.queue = list()
        # user input value for maxSize
        self.maxSize = maxSize
        self.head = 0
        self.tail = 0

    # add element to the queue
    def enqueue(self, data):
        # if queue is full
        if self.size() == (self.maxSize - 1):
            return ("Queue is full!")
        else:
            # add element to the queue
            self.queue.append(data)
            # increment the tail pointer
            self.tail = (self.tail + 1) % self.maxSize
            return True

    # remove element from the queue
    def dequeue(self):
        # if queue is empty
        if self.size() == 0:
            return ("Queue is empty!")
        else:
            # fetch data
            data = self.queue[self.head]
            # increment head
            self.head = (self.head + 1) % self.maxSize
            return data

    # find the size of the queue
    def size(self):
        if self.tail >= self.head:
            qSize = self.tail - self.head
        else:
            qSize = self.maxSize - (self.head - self.tail)
        # return the size of the queue
        return qSize


# input 7 for the size or anything else
size = input("Enter the size of the Circular Queue: ")
q = CircularQueue(int(size))

# change the enqueue and dequeue statements as you want
print(q.dequeue(10))
print(q.head)
print(q.tail)
print()
print()
