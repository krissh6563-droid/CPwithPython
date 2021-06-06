# declaration of tree node
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)

# create a binary search tree class


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# preorder traversal
def preOrder(root):
    if root:
        print(root.info)
        preOrder(root.left)
        preOrder(root.right)

# postorder traversal


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info)


# def inorder traversal
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.info)
        inOrder(root.right)


tree = BinarySearchTree()
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    tree.create(arr[i])

preOrder(tree.root)
inOrder(tree.root)
postOrder(tree.root)
