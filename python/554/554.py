# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 0027 22:29
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 554.py
# @Software: PyCharm
"""
你的面前有一堵方形的、由多行砖块组成的砖墙。 这些砖块高度相同但是宽度不同。你现在要画一条自顶向下的、穿过最少砖块的垂线。

砖墙由行的列表表示。 每一行都是一个代表从左至右每块砖的宽度的整数列表。

如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。

你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。

 

示例：

输入: [[1,2,2,1],
      [3,1,2],
      [1,3,2],
      [2,4],
      [3,1,2],
      [1,3,1,1]]

输出: 2

解释:

 

提示：

每一行砖块的宽度之和应该相等，并且不能超过 INT_MAX。
每一行砖块的数量在 [1,10,000] 范围内， 墙的高度在 [1,10,000] 范围内， 总的砖块数量不超过 20,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/brick-wall
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def leastBricks(self, wall: list) -> int:
        my_dict={}
        for item_wall in wall:
            sum=0
            for i in range(len(item_wall)-1):
                sum=sum+item_wall[i]
                if sum in my_dict.keys():
                    my_dict[sum]+=1
                else:
                    my_dict[sum]=1
        res=len(wall)
        for item in my_dict.items():
            res=min(res,len(wall)-item[1])
        return res

    def leastBricks2(self, wall: list) -> int:
        sum_list=[]
        for row in wall:
            sum=0
            for i in range(len(row)-1):
                sum+=row[i]
                sum_list.append(sum)
        counts=collections.Counter(sum_list)
        height=len(wall)
        res=height
        for item in counts.items():
            res=min(res,height-item[1])
        return res
if __name__=="__main__":
    nums = [[1,2,1],
            [3,1],
            [2,2]]
    so=Solution()
    a=so.leastBricks2(nums)
    print(a)