#MyStackpy
stack = []  # Internal list to store stack items
capacity = None  # Optional maximum capacity of the stack

## Functionality
class MyStack:
    def __init__(self, capacity=None):
        """
        Initialize an empty stack with an optional capacity.
        Precondition: `capacity` is a positive integer or None (no limit).
        Postcondition: An empty stack is created, optionally with a maximum capacity.
        """
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        """
        Add an item to the top of the stack if there is space available.
        Precondition: The stack is not full (if capacity is set).
        Postcondition: If successful, the stack is 1 item larger, and the top contains the added item.
        :return: True if the item was added, False if the stack is full.
        """
        if self.capacity is None or len(self.stack) < self.capacity:
            self.stack.append(item)
            return True
        return False

    def pop(self):
        """
        Remove and return the item at the top of the stack.
        Precondition: The stack is not empty.
        Postcondition: The stack is 1 item smaller, and the top item is removed.
        :return: A tuple containing the removed item and True if successful, or (None, False) if the stack is empty.
        """
        if self.stack:
            return self.stack.pop(), True
        return None, False

    def isEmpty(self):
        """
        Check if the stack is empty.
        Precondition: None.
        Postcondition: The stack remains unchanged.
        :return: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def getTop(self):
        """
        Retrieve the item at the top of the stack without removing it.
        Precondition: The stack is not empty.
        Postcondition: The stack remains unchanged.
        :return: A tuple containing the top item and True if successful, or (None, False) if the stack is empty.
        """
        if self.stack:
            return self.stack[-1], True
        return None, False

    def save(self):
        """
        Save the current state of the stack as a string representation.
        Precondition: None.
        Postcondition: The stack remains unchanged.
        :return: A string representation of the stack.
        """
        return str(self.stack)

    def load(self, items):
        """
        Load a list of items into the stack, replacing the current stack.
        Note: This method does not enforce the capacity limit.
        Precondition: `items` is a valid iterable (e.g., list, tuple).
        Postcondition: The stack contains the items from the input iterable.
        """
        self.stack = list(items)