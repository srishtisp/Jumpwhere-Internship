#Problem 701

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root=TreeNode(val)
            return root
        if root.val<val:
            root.right=self.insertIntoBST(root.right,val)
        else:
            root.left=self.insertIntoBST(root.left,val)
        return root