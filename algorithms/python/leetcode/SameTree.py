#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical
and the nodes have the same value.
https://oj.leetcode.com/problems/same-tree/
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val == q.val and self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right):
            return True
        else:
            return False

if __name__ == '__main__':
    r1 = TreeNode(1)
    r2 = TreeNode(2)
    r3 = TreeNode(3)
    r4 = TreeNode(2)
    r1.left = r2
    r2.right = r3
    r4.right = r3
    test_case = [
        [r1, r3],
        [r2, r4],
        [r3, r4]
        ]
    for t in test_case:
        print(Solution().isSameTree(t[0], t[1]))
