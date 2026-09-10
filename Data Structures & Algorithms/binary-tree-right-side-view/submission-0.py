class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        
        while q:
            lenght = len(q)
            for i in range(lenght):
                node = q.popleft()
                if i == lenght - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res