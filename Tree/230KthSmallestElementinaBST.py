from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       self.count = 0
       self.result = None

       def inorder(node):
          if not node or self.result is not None :
             return
          inorder (node.left) 
        #到底就沒有辦法再回上面 就往下
          self.count += 1
          if self.count == k:
             self.result = node.val 
             return 
          inorder (node.right)
       inorder (root)
       return self
        

       
        