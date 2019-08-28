__author__ = 'Administrator'

class Solution(object):
    '''
        :param string
        :return boolean
    '''
    def isPalindrome(self,s):

        i,j=0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if(s[i].lower()!=s[j].lower()):
                return False
            i,j=i+1,j-1
        return True

if __name__=="__main__":
    s=Solution()
    print (s.isPalindrome("A man, a plan, a canal: Panama"))


'''
    python知识：
    isalnum():检测字符串是否由字符和数字构成

'''