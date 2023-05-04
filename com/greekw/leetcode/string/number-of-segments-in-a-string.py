__author__ = 'Administrator'
# Time:  O(n)
# Space: O(1)

# Count the number of segments in a string,
# where a segment is defined to be a contiguous
# sequence of non-space characters.
#
# Please note that the string does not
# contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5

class Solution(object):

    def countSegments(self,s):
        '''
        :param s:
        :return:
        '''
        result=int(len(s) and s[-1]!= ' ')
        for i in range(1,len(s)):
            if(s[i]==' ' and s[i-1]!=' ')
                result+=1

        return  result

    def countSegments2(self,s):

        '''

        :param s:
        :return:
        '''
        return  len([i for i in s.strip().split(' ') if i])


'''
    pyton知识：
    range()和xrange():两者用法完全相同， 前者生成一个生成器，后者生成一个list，要生成很大数字列表时，xrange比range性能更优，
    不需要提前开辟一块大的内存空间



'''