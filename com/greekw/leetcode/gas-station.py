__author__ = 'greek'
# -*- coding:utf-8 -*-
#!/user/bin/pyhton3

'''
134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station’s index if you can travel around the circuit once, otherwise return -1
Note:
The solution is guaranteed to be unique.
#参考地址：http://blog.csdn.net/ljiabin/article/category/1355878
'''

class Solution:
    def canComputeCircute(self,gas,cost):
        #依次遍历每个加油站
        for i in range(len(gas)):
            j=i
            tmp=gas[j]
            # 如果当前加油站能到达下一站，则减去本次消耗的油
            while(tmp>=cost[j]):
                tmp-=cost[j]
                #到达下一站后若与起始点相同，则返回
                j=(j+1)%len(gas)
                if(j==i):
                    return i
                #到达下一站后继续加油前进
                tmp+=gas[i]
        return -1

if __name__ == "__main__":
    s=Solution()
    print(s.canComputeCircute([1, 2, 3], [3, 2, 1]))