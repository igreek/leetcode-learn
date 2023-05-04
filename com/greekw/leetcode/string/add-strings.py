# Time:  O(n)
# Space: O(1)

# Given two non-negative numbers num1 and num2 represented as string,
# return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or
# convert the inputs to integer directly.

class Solution(object):

    def addStrings(self,num1,num2):

        '''
        :param num1:
        :param num2:
        :return:
        '''
        result=[]
        i,j,carry=len(num1)-1,len(num2)-1,0
        while i>=0 or j>=0 or carry:
            if i>=0:
                carry+=ord(num1[i])-ord('0');
                i-=1
            if j>=0:
                carry+=ord(num2[j])-ord('0');
                j-=1
            result.append(str(carry%10))
            carry/=10
        result.reverse()
        return "".join(result)

if __name__=="__main__":
    s=Solution()
    print (s.addStrings('1','2'))



'''
    pyton֪ʶ��

        ord():��chr()����������8λ��ASCII�ַ�������unichr()����������Unicode���󣩵���Ժ���������һ���ַ�������Ϊ1���ַ�������Ϊ������
        ���ض�Ӧ��ASCII��ֵ������Unicode��ֵ�����������Unicode�ַ����������Python���巶Χ���������һ��TypeError���쳣��

        ���Ƶĺ���Ϊ��chr()������һ����Χ��range��256���ڵģ�����0��255������������������һ����Ӧ���ַ���unichr()����һ����ֻ�������ص���Unicode�ַ�


'''