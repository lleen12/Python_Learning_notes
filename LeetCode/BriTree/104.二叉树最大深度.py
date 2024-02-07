# [104]二叉树的最大深度
"""
给定一个二叉树root, 返回其最大深度。
二叉树的最大深度，是指从根节点到最远叶子节点的最长路径上的节点数。
示例1：
输入：root = [3, 9, 20, null, null, 15, 7]
输出：3
示例2：
输入：root = [1, null, 2]
输出：2
"""
"""
LeetCode提交区域的代码中，需要先将数组转换成二叉树，然后再进行求解。因为LeetCode的测试用例通常以二叉树的形式给出。
"""
#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  # def maxDepth(self, root:Optional[TreeNode]) -> int:
  def maxDepth(self, root):
    if root is None:
      return 0
    else:
      left_height = self.maxDepth(root.left)
      right_height = self.maxDepth(root.right)
      return max(left_height, right_height) + 1
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
  # root = [3, 9, 'null', 'null', 15, 7]
  # a = TreeNode()
  # s = Solution()
  # print(s.maxDepth(root))
  # 正确
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)
  a = TreeNode()
  s = Solution()
  print(s.maxDepth(root))


















      
