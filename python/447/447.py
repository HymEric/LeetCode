# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 0026 19:36
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 447.py
# @Software: PyCharm
"""
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-boomerangs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def numberOfBoomerangs(self, points: list) -> int:
        def fun(x1,y1):
            d=collections.Counter((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) for x2,y2 in points)
            return sum(t*(t-1) for t in d.values())
        return sum(fun(x1,y1) for x1,y1 in points)
    # method: hashMap, dicts to record
    def numberOfBoomerangs2(self, points: list) -> int:
        res = 0
        for x1,y1 in points:
            dicts = {}
            for x2,y2 in points:
                k=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
                if k==0:
                    continue
                if k in dicts.keys():
                    dicts[k]+=1
                else:
                    dicts[k]=1
            for i in dicts.values():
                res += i * (i - 1)
        return res
if __name__=="__main__":
    s= [[0,0],[1,0],[2,0]]
    so=Solution()
    a=so.numberOfBoomerangs2(s)
    print(a)