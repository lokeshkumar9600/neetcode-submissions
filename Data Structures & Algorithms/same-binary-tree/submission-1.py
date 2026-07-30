# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                temp_1 = q1.popleft()
                temp_2 = q2.popleft()
                if temp_1 is None and temp_2 is None:
                    continue
                if temp_1 is None or temp_2 is None or temp_1.val != temp_2.val:
                    return False
                
                q1.append(temp_1.left)
                q1.append(temp_1.right)
                q2.append(temp_2.left)
                q2.append(temp_2.right)
        
        return True
            



        