class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


    def insert(self, value: int):
        if self.root is None:
            self.root = TreeNode(value)
            return True
        current = self.root

        while True:
            if value < current.data:
                if current.left is None:
                    current.left = TreeNode(value)
                    return True
                current = current.left

            elif value > current.data:
                if current.right is None:
                    current.right = TreeNode(value)
                    return True
                current = current.right

            else:
                return False
        

    def display(self):
        result = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.data)
                traverse(node.right)

        traverse(self.root)
        return result

    
    def search(self, value: int):
        if self.root is None:
            return False
        current = self.root

        while True:
            if value < current.data:
                if current.left is None:
                    return False
                current = current.left

            elif value > current.data:
                if current.right is None:
                    return False
                current = current.right

            elif value == current.data:
                return True
            
            else:
                return False
            

    def delete(self, value: int):
        def _delete_node(node, value):
            if node is None:
                return node
            
            if value < node.data:
                node.left = _delete_node(node.left, value)
            
            elif value > node.data:
                node.right = _delete_node(node.right, value)
            
            else:
                if node.left is None:
                    return node.right
            
                elif node.right is None:
                    return node.left
                
                temp = node.right
            
                while temp.left:
                    temp = temp.left
                node.data = temp.data
                node.right = _delete_node(node.right, temp.data)
            
            return node

        self.root = _delete_node(self.root, value)
