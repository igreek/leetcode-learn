__author__ = 'Administrator'
# Time:  O(n)
# Space: O(1)
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].
#


class Solution(object):

    def removeDuplicates(self,A):
        '''

        :param A:
        :return:
        '''
        if not A:
            return 0
        last,i=0,1
        while i<len(A):
            if A[last]!=A[i]:
                last+=1
                A[last]=A[i]
            i+=1
        return last+1

if __name__=="__main__":
    s=Solution()
    print(s.removeDuplicates([1,1,2]))
