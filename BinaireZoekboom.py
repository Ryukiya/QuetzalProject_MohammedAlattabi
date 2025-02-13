#Binairezoekboom.py
# Helper function to create a tree item
def createTreeItem(key, val):
    """
    Create a dictionary representing a tree item.
    :param key: The key of the item.
    :param val: The value of the item.
    :return: A dictionary with the key and value.
    """
    return {"key": key, "value": val}

# ADT BST (Binary Search Tree)
class BST:
    class Node:
        def __init__(self, item):
            """
            Initialize a node with a tree item.
            :param item: The tree item (dictionary with "key" and "value").
            """
            self.item = item
            self.left = None  # Left child
            self.right = None  # Right child

    def __init__(self):
        """
        Initialize an empty BST.
        Precondition: None.
        Postcondition: An empty BST is created.
        """
        self.root = None  # Root of the tree
        self.size = 0  # Number of nodes in the tree

    def isEmpty(self):
        """
        Check if the BST is empty.
        Precondition: None.
        Postcondition: The BST remains unchanged.
        :return: True if the BST is empty, False otherwise.
        """
        return self.root is None

    def searchTreeInsert(self, item):
        """
        Insert a new item into the BST.
        Precondition: The item's key must not already exist in the BST.
        Postcondition: The BST contains the new item, and its size is incremented by 1.
        :param item: The item to insert (dictionary with "key" and "value").
        :return: True if the insertion was successful, False otherwise.
        """
        if self.searchTreeRetrieve(item["key"])[0]:
            return False  # Key already exists

        self.size += 1
        if self.isEmpty():
            self.root = self.Node(item)
            return True

        current = self.root
        while True:
            if item["key"] < current.item["key"]:
                if current.left is None:
                    current.left = self.Node(item)
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = self.Node(item)
                    return True
                current = current.right

    def searchTreeRetrieve(self, key):
        """
        Retrieve an item from the BST by its key.
        Precondition: None.
        Postcondition: The BST remains unchanged.
        :param key: The key of the item to retrieve.
        :return: A tuple containing the key and True if found, or (False, None) if not found.
        """
        if self.isEmpty():
            return False, None

        current = self.root
        while current:
            if key == current.item["key"]:
                return key, True  # Key found
            elif key < current.item["key"]:
                current = current.left
            else:
                current = current.right
        return False, None  # Key not found

    def searchTreeDelete(self, key):
        """
        Delete an item from the BST by its key.
        Precondition: The key must exist in the BST.
        Postcondition: The BST no longer contains the item, and its size is decremented by 1.
        :param key: The key of the item to delete.
        :return: True if the deletion was successful, False otherwise.
        """
        if self.isEmpty():
            return False

        parent = None
        current = self.root
        is_left = True

        # Find the node to delete
        while current and current.item["key"] != key:
            parent = current
            if key < current.item["key"]:
                current = current.left
                is_left = True
            else:
                current = current.right
                is_left = False

        if not current:
            return False  # Key not found

        self.size -= 1

        # Case 1: Node has no children
        if not current.left and not current.right:
            if parent is None:
                self.root = None
            elif is_left:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node has only a right child
        elif not current.left:
            if parent is None:
                self.root = current.right
            elif is_left:
                parent.left = current.right
            else:
                parent.right = current.right

        # Case 3: Node has only a left child
        elif not current.right:
            if parent is None:
                self.root = current.left
            elif is_left:
                parent.left = current.left
            else:
                parent.right = current.left

        # Case 4: Node has two children
        else:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            if successor_parent != current:
                successor_parent.left = successor.right
                successor.right = current.right
            successor.left = current.left

            if parent is None:
                self.root = successor
            elif is_left:
                parent.left = successor
            else:
                parent.right = successor

        return True

    def inorderTraverse(self, func):
        """
        Perform an inorder traversal of the BST and apply a function to each node's key.
        Precondition: None.
        Postcondition: The BST remains unchanged.
        :param func: A function to apply to each node's key.
        """
        def _inorder(node):
            if node:
                _inorder(node.left)
                func(node.item["key"])
                _inorder(node.right)
        _inorder(self.root)

    def save(self):
        """
        Save the BST as a string representation.
        Precondition: None.
        Postcondition: The BST remains unchanged.
        :return: A string representation of the BST.
        """
        if self.isEmpty():
            return None

        def create_dict(node):
            if not node:
                return None
            children = [create_dict(node.left), create_dict(node.right)]
            if not any(children):
                return {'root': node.item["key"]}
            return {'root': node.item["key"], 'children': children}

        result = create_dict(self.root)
        if result is None:
            return None
        return self._dict_to_string(result)

    def _dict_to_string(self, d):
        """
        Convert a dictionary representation of the BST to a string.
        :param d: The dictionary to convert.
        :return: A string representation of the dictionary.
        """
        if d is None:
            return 'None'
        if 'children' not in d:
            return "{'root': " + str(d['root']) + "}"
        children_str = '[' + ','.join(self._dict_to_string(c) for c in d['children']) + ']'
        return "{'root': " + str(d['root']) + ",'children':" + children_str + "}"

    def load(self, tree_dict):
        """
        Load a BST from a dictionary representation.
        Precondition: `tree_dict` is a valid dictionary representation of a BST.
        Postcondition: The BST is replaced with the tree represented by `tree_dict`.
        :param tree_dict: The dictionary representation of the BST.
        """
        if not tree_dict:
            self.root = None
            self.size = 0
            return

        def create_node(d):
            if not d:
                return None
            node = self.Node(createTreeItem(d['root'], d['root']))
            children = d.get('children', [])

            if len(children) > 0:
                node.left = create_node(children[0])
            if len(children) > 1:
                node.right = create_node(children[1])

            return node

        self.root = create_node(tree_dict)

        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        self.size = count_nodes(self.root)