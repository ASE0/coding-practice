# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeList = []
        self.dfs(root, nodeList)
        nodeList = sorted(nodeList)
        return nodeList[k - 1]
    def dfs(self, root, nodeList):
        if root:
            nodeList.append(root.val)
            self.dfs(root.left, nodeList)
            self.dfs(root.right, nodeList)
        return nodeList