#MyQueue.py
_items = []  # Internal list to store queue items
_capacity = None  # Maximum capacity of the queue

## Functionality
class MyQueue:
    def __init__(self, capacity=None):
        """
        Initialize an empty queue with a specified capacity.
        Precondition: `capacity` is a positive integer.
        Postcondition: An empty queue is created with the given capacity.
        """
        self._items = []
        self._capacity = capacity

    def isEmpty(self):
        """
        Check if the queue is empty.
        Precondition: None.
        Postcondition: The queue remains unchanged.
        :return: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def enqueue(self, item):
        """
        Add an item to the back of the queue if there is space available.
        Precondition: The queue is not full.
        Postcondition: If successful, the queue is 1 item larger, and the item is added to the back.
        :return: True if the item was added, False if the queue is full.
        """
        if len(self._items) >= self._capacity:
            return False
        self._items.insert(0, item)
        return True

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        Precondition: The queue is not empty.
        Postcondition: The queue is 1 item smaller, and the front item is removed.
        :return: A tuple containing the removed item and True if successful, or (False, False) if the queue is empty.
        """
        if self.isEmpty():
            return False, False
        item = self._items.pop()
        return item, True

    def getFront(self):
        """
        Retrieve the item at the front of the queue without removing it.
        Precondition: The queue is not empty.
        Postcondition: The queue remains unchanged.
        :return: A tuple containing the front item and True if successful, or (False, False) if the queue is empty.
        """
        if self.isEmpty():
            return False, False
        return self._items[-1], True

    def save(self):
        """
        Save the current state of the queue as a list.
        Precondition: None.
        Postcondition: The queue remains unchanged.
        :return: A list representation of the queue.
        """
        return self._items

    def load(self, items):
        """
        Load a list of items into the queue, replacing the current queue.
        Note: This method does not enforce the capacity limit.
        Precondition: `items` is a valid iterable (e.g., list, tuple).
        Postcondition: The queue contains the items from the input iterable.
        """
        self._items = list(items)