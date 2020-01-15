class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

# Root -> Left -> Right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)
            res = res + left + right
        return res

# Left -> Right -> Root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

    def leftHeight(self, root):
        if root:
            return 1 + self.leftHeight(root.left)
        else:
            return 0

    def rightHeight(self, root):
        if root:
            return 1 + self.rightHeight(root.right)
        else:
            return 0

    def height(self, root):
        return max(self.leftHeight(root), self.rightHeight(root))


root = TreeNode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print('In-Order  '),
print(root.inorderTraversal(root))
print('Pre-Order '),
print(root.preorderTraversal(root))
print('Post-Order'),
print(root.postorderTraversal(root))

print('Height '),
print(root.height(root))
