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
    pyton知识：

        ord():是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，
        返回对应的ASCII数值，或者Unicode数值，如果所给的Unicode字符超出了你的Python定义范围，则会引发一个TypeError的异常。

        类似的函数为：chr()函数用一个范围在range（256）内的（就是0～255）整数作参数，返回一个对应的字符。unichr()跟它一样，只不过返回的是Unicode字符


'''