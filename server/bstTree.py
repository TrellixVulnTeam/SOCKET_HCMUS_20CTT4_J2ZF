class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLtree(object):
    notFound = "not found!!!"
    def insert(self, root, data, keyName):
        # implement normal BST tree
        if not root:
            return TreeNode(data)
        elif data[str(keyName)] < root.val[str(keyName)]:
            root.left = self.insert(root.left, data, keyName)
        else:
            root.right = self.insert(root.right, data, keyName)
        # update height tree
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        # get balance factor
        balance = self.getBalance(root)
        # if node is imbalance then try regain balance
        # left left imbalance
        if balance > 1 and data[str(keyName)] < root.left.val[str(keyName)]:
            return self.rightRotate(root)
        # right right imbalance
        if balance < -1 and data[str(keyName)] > root.right.val[str(keyName)]:
            return self.leftRotate(root)
        # left right imbalance (LR -(left rotate)->LL -(right rotate)->)
        if balance > 1 and data[str(keyName)] > root.left.val[str(keyName)]:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # right left imbalance (RL -(right rotate)->RR-(left rotate)->)
        if balance < -1 and data[str(keyName)] < root.right.val[str(keyName)]:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def rightRotate(self,P):
        #             P                           L1
        #           /   \                       /    \
        #         L1    R1                     L2     P
        #        /  \                         / \    / \
        #       L2  R2               =>      L3 R3  R2 R1
        #      / \
        #     L3  R3
        L1 = P.left
        R2 = L1.right
        # perform rotation
        L1.right = P
        P.left = R2
        # update height
        P.height = 1 + max(self.getHeight(P.left),
                        self.getHeight(P.right))
        L1.height = 1 + max(self.getHeight(L1.left),
                        self.getHeight(L1.right))               
        return L1
    def leftRotate(self, P):
        #           P                             R1
        #          / \                           /  \
        #         L1  R1                        P    R2
        #            /  \           =>         / \   / \
        #           L2  R2                    L1 L2 L3 R3
        #               / \
        #              L3  R3
        R1 = P.right
        L2 = R1.left
        # perform rotation
        R1.left = P
        P.right = L2
        # update height
        P.height = 1 + max(self.getHeight(P.left),
                        self.getHeight(P.right))
        R1.height = 1 + max(self.getHeight(R1.left),
                        self.getHeight(R1.right))   
        return R1
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
    def search(self, root, name ,keyName):
        if not root:
            return self.notFound
        if root.val[str(keyName)] > str(name):
            return self.search(root.left, name, keyName)
        elif root.val[str(keyName)] < str(name):
            return self.search(root.right, name, keyName)
        else:
            return root