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
    pyton֪ʶ��
    range()��xrange():�����÷���ȫ��ͬ�� ǰ������һ������������������һ��list��Ҫ���ɺܴ������б�ʱ��xrange��range���ܸ��ţ�
    ����Ҫ��ǰ����һ�����ڴ�ռ�



'''