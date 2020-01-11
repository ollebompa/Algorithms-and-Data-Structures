class Node:
    """
    Class to define nodes making up the tree
    """
    def __init__(self, data):
        """
        Initiate node.
        :param data: Value associated with node.
        """
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        """
        Initiate node.
        :param data: Value associated with node.
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data


    def find_value(self, val):
        """
        Search tree for given value.
        :param val: Value to be searched for.
        """
        if val < self.data:
            if self.left is None:
                return f'{val} was not found'
            return self.left.find_value(val)
        elif val > self.data:
            if self.right is None:
                return f'{val} was not found'
            return self.right.find_value(val)
        else:
            return f'{self.data} was found'


root = Node(10)
root.insert(5)
root.insert(12)
root.insert(1)
print(root.find_value(12))
print(root.find_value(1))
print(root.find_value(7))
