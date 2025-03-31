# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(root: TreeNode) -> bool:
        def helper(node, min_val, max_val):
            # 基本情況：當節點為空時，返回 True
            if not node:
                return True
            
            # 當節點值不在合法範圍內時，返回 False
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # 遞歸檢查左右子樹
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
        
        return helper(root, float('-inf'), float('inf'))
       
        