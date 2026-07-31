# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        while queue:
            rightSide = None
            qlen = len(queue)
            for i in range(qlen):
                x = queue.popleft()
                if x:
                    rightSide = x
                    queue.append(x.left)
                    queue.append(x.right)
            
            if rightSide:
                ans.append(rightSide.val)

        return ans 