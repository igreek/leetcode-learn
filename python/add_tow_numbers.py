__author__ = 'greek'
# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
  连个数的链表相加，需处理进位
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def addTowNumbers(self,l1,l2):

        dummy=ListNode(0)
        current,carry=dummy,0
        while l1 or l2:
            val=carry
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            carry,val=val/10,val%10
            current.next=ListNode(val)
            current=current.next
        if carry==1:
            current.next=ListNode(1)

        return dummy.next

if __name__=='__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result=Solution.addTowNumbers(a,b)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))