class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([(root, float('-inf'), float('inf'))])
        while q:
            node, low, high = q.popleft()
            if not node:
                continue
            if not (low < node.val < high):
                return False
            q.append((node.left, low, node.val))
            q.append((node.right, node.val, high))
        return True