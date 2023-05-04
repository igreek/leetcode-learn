__author__ = 'greekw'
# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
  leetcode 堆寻找最最小K对数
'''
#python3d  http://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p05_implement_a_priority_queue.html
import heapq
class Solution(object):
    def K_SmallestPair(self,nums1,nums2,k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs

if __name__ == "__main__":
    s=Solution()
    nums1=[1,1,2]
    nums2=[1,2,3]
    k=2
    print(s.K_SmallestPair(nums1,nums2,k))