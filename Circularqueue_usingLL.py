# Python3 program for insertion and
# deletion in Circular Queue

# Structure of a Node
class Node:
    def __init__(self):
        self.data = None
        self.next = None


class Queue:
    def __init__(self):
        front = None
        rear = None


# Function to create Circular queue
def enQueue(q, value):
    temp = Node()
    temp.data = value
    if q.front is None:
        q.front = temp
    else:
        q.rear.next = temp

    q.rear = temp
    q.rear.next = q.front


# Function to delete element from
# Circular Queue
def deQueue(q):
    if q.front is None:
        print("Queue is empty")
        return 0

    # If this is the last node to be deleted
    value = None  # Value to be dequeued
    if q.front == q.rear:
        value = q.front.data
        q.front = None
        q.rear = None
    else:  # There are more than one node
        temp = q.front
        value = temp.data
        q.front = q.front.next
        q.rear.next = q.front

    return value


# Function displaying the elements
# of Circular Queue
def displayQueue(q):
    temp = q.front
    print("Elements in Circular Queue are: ",
          end=" ")
    while temp.next != q.front:
        print(temp.data, end=" ")
        temp = temp.next
    print(temp.data)


# Driver Code
if __name__ == '__main__':
    # Create a queue and initialize
    # front and rear
    q = Queue()
    q.front = q.rear = None

    # Inserting elements in Circular Queue
    enQueue(q, 14)
    enQueue(q, 22)
    enQueue(q, 6)

    # Display elements present in
    # Circular Queue
    displayQueue(q)

    # Deleting elements from Circular Queue
    print("Deleted value = ", deQueue(q))
    print("Deleted value = ", deQueue(q))

    # Remaining elements in Circular Queue
    displayQueue(q)

    enQueue(q, 9)
    enQueue(q, 20)
    displayQueue(q)
