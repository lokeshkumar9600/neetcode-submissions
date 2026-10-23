# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        
        q = deque()
        q.append(root)
        ans = []

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if temp:
                ans.append(temp[-1])
        

        return ans


                
                




        
        