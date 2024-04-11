class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.weight = len(value)
    
    def __repr__(self) -> str:
        return f"Node({self.value})"
    
    def update_weight(self):
        self.weight = len(self.value) + (self.left.weight if self.left else 0) + (self.right.weight if self.right else 0)


class Rope():

    # Costructor should initialize the rope with an optional initial string. It should build balanced 
    # tree structure (AVL or red-black?).
    # Create a new root node
    def __init__(self, s='') -> None:
        self.root = self._build_rope(s)
        print("rope created")
    

    def _build_rope(self, s):
        if not s:
            return None;

        mid = len(s) // 2
        node = Node(s[mid])
        node.left = self._build_rope(s[:mid])
        node.right = self._build_rope(s[mid+1:])
        return node;
    
    def insert_char(self, index, char):
        self.root = self._insert_char(self.root, index, char)
    
    def _insert_char(self, node, index, char):
        if node is None:
            return Node(char)

        if index <= node.weight:
            node.left = self._insert_char(node.left, index, char)
        else:
            node.right = self._insert_char(node.right, index - node.weight, char)

        node.update_weight() 

        return node



    def __repr__(self):
        return self._repr_helper(self.root)
    
    def _repr_helper(self, node):
        if node is None:
            return ''
        return self._repr_helper(node.left) + node.value + self._repr_helper(node.right)


# Example usage:
text = "Hello_my_name_is_Simon."
rope = Rope(text)
print("Original Rope:", rope)

# Inserting a character '!' at index 5
rope.insert_char(5, '!')
print("After insertion:", rope)


