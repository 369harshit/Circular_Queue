class CircularQueue():

    # constructor of CircularQueue class
    # initializing the class
    def __init__(self, queue_size):
        self.queue_size = queue_size

        # initializing queue with none
        self.queue = [None for i in range(queue_size)]
        self.front = self.rear = -1

    # function to insert element
    # to a circular queue
    def enqueue(self, value):

        # check if queue is full
        if (self.rear + 1) % self.queue_size == self.queue_size:
            print(" Queue is Full\n")

        # check if queue is empty
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:

            # next position of rear
            self.rear = (self.rear + 1) % self.queue_size
            self.queue[self.rear] = value

    # function to remove element
    # to a circular queue
    def dequeue(self):

        # check if the queue is empty
        if self.front == -1:
            print("Queue is Empty\n")

        # check for a single element
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.queue_size
            return temp

    # function to display the circular
    # queue elements
    def show_current_queue(self):

        # check if queue is empty
        if self.front == -1:
            print("Queue is Empty")

        elif self.rear >= self.front:
            print("current circular queue:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("current circular queue:", end=" ")
            for i in range(self.front, self.queue_size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

        if (self.rear + 1) % self.queue_size == self.front:
            print("\nCircular Queue Full.")


# create an object of
# the circular queue class
queue_object = CircularQueue(5)
queue_object.show_current_queue()

# add elements to the queue
queue_object.enqueue(1)
queue_object.enqueue(2)
queue_object.enqueue(3)
queue_object.enqueue(4)

# show current queue
queue_object.show_current_queue()

# print deleted elements of the queue
print("Value removed from queue:", queue_object.dequeue())
print("Value removed from queue:", queue_object.dequeue())

# show current queue
queue_object.show_current_queue()

# adding this element to
# the queue
queue_object.enqueue(5)
queue_object.enqueue(6)

# adding this element to
# the queue makes it full
queue_object.enqueue(7)

# show current queue
queue_object.show_current_queue()
