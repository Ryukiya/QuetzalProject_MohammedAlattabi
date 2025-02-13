#CirculaireGelinkteChain
class CirculaireGelinkteChain:
    class Node:
        def __init__(self, data=None):
            """
            Initialize a node with data and a reference to the next node.
            :param data: The data to store in the node.
            """
            self.data = data
            self.next = None  # Reference to the next node

    def __init__(self):
        """
        Initialize an empty linked list.
        Precondition: None.
        Postcondition: An empty linked list is created.
        """
        self.head = None  # Reference to the first node
        self.size = 0  # Number of nodes in the list

    def isEmpty(self):
        """
        Check if the linked list is empty.
        Precondition: None.
        Postcondition: The linked list remains unchanged.
        :return: True if the list is empty, False otherwise.
        """
        return self.head is None

    def getLength(self):
        """
        Get the number of nodes in the linked list.
        Precondition: None.
        Postcondition: The linked list remains unchanged.
        :return: The number of nodes in the list.
        """
        return self.size

    def retrieve(self, position):
        """
        Retrieve the data at a specific position in the linked list.
        Precondition: The position must be valid (1 ≤ position ≤ size).
        Postcondition: The linked list remains unchanged.
        :param position: The position of the node to retrieve.
        :return: A tuple containing the data and True if successful, or (None, False) if the position is invalid.
        """
        if position < 1 or position > self.size:
            return None, False  # Position out of bounds

        current = self.head
        for _ in range(1, position):
            current = current.next
        return current.data, True

    def insert(self, position, data):
        """
        Insert a new node with data at a specific position in the linked list.
        Precondition: The position must be valid (1 ≤ position ≤ size + 1).
        Postcondition: The linked list contains the new node, and its size is incremented by 1.
        :param position: The position at which to insert the new node.
        :param data: The data to store in the new node.
        :return: True if the insertion was successful, False otherwise.
        """
        if position < 1 or position > self.size + 1:
            return False  # Invalid position

        new_node = self.Node(data)

        # Insert at the beginning
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            # Insert at other positions
            current = self.head
            for _ in range(1, position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1
        return True

    def delete(self, position):
        """
        Delete a node at a specific position in the linked list.
        Precondition: The position must be valid (1 ≤ position ≤ size).
        Postcondition: The linked list no longer contains the node, and its size is decremented by 1.
        :param position: The position of the node to delete.
        :return: True if the deletion was successful, False otherwise.
        """
        if position < 1 or position > self.size:
            return False  # Invalid position

        # Delete the first node
        if position == 1:
            self.head = self.head.next
        else:
            # Delete from other positions
            current = self.head
            for _ in range(1, position - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1
        return True

    def save(self):
        """
        Save the linked list as a list of data.
        Precondition: None.
        Postcondition: The linked list remains unchanged.
        :return: A list containing the data of all nodes in the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def load(self, data):
        """
        Load a list of data into the linked list, replacing the current list.
        Precondition: `data` is a valid iterable (e.g., list, tuple).
        Postcondition: The linked list contains nodes with the data from the input iterable.
        :param data: The list of data to load into the linked list.
        """
        self.head = None
        self.size = 0

        for item in data:
            new_node = self.Node(item)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            self.size += 1