class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data 

def preorder(root):
    if root == None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')

def build_tree():
    """
             10
           /    \
          5      8
         / \    / \
        3   9  1   2
    """
    root = Node(10)
    root.left = Node(5)
    root.right = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(9)
    root.right.left = Node(1)
    root.right.right = Node(2)
    return root

if __name__ == "__main__":
    t = build_tree()

    print("{:10s}".format("Preorder:"), end=" ")
    preorder(t)
    print("\n{:10s} {:20s}\n".format("Expected:", "10 5 3 9 8 1 2"))
    
    print("{:10s}".format("Inorder:"), end=" ")
    inorder(t)
    print("\n{:10s} {:20s}\n".format("Expected:", "3 5 9 10 1 8 2"))
    
    print("{:10s}".format("Postorder:"), end=" ")
    postorder(t)
    print("\n{:10s} {:20s}\n".format("Expected:", "3 9 5 1 2 8 10"))
