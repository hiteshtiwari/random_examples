class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root):
    if root == None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)