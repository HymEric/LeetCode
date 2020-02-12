# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 0001 12:01
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 407.py
# @Software: PyCharm
"""
给定一个 m x n 的矩阵，其中的值均为正整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

 

说明:

m 和 n 都是小于110的整数。每一个单位的高度都大于 0 且小于 20000。

 

示例：

给出如下 3x6 的高度图:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

返回 4。


如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。

 



下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
class Solution:
    def trapRainWater(self, heightMap:list) -> int:
        if not heightMap:
            return 0
        row,col=len(heightMap),len(heightMap[0])
        ans=0 # result
        heap=[]
        visited=[[0 for _ in range(col)] for _ in range(row)] #记录是否访问过
        # 邻居-上下左右的坐标
        surround=[(-1,0),(1,0),(0,-1),(0,1)]
        # 坐标验证是否在图矩阵内
        def in_area(m,n):
            return 0<=m<row and 0<=n<col

        for i in range(row): #堆 优先队列, 先将最外层第一圈装入
            heap.append([heightMap[i][0],i,0]) #如堆，[值，坐标x，坐标y]
            heap.append([heightMap[i][col-1],i,col-1])
            visited[i][0]=1
            visited[i][col-1]=1
        for j in range(1,col-1):
            heap.append([heightMap[0][j],0,j])
            heap.append([heightMap[row-1][j],row-1,j])
            visited[0][j]=1
            visited[row-1][j]=1
        heapq.heapify(heap) # 小根堆，每次都弹出最小的

        while heap:
            height,x,y=heapq.heappop(heap)
            for dx,dy in surround:
                nx,ny=x+dx,y+dy
                if in_area(nx,ny) and not visited[nx][ny]:
                    cur=[max(height,heightMap[nx][ny]),nx,ny]
                    ans+=max(0,height-heightMap[nx][ny])
                    heapq.heappush(heap,cur)
                    visited[nx][ny]=1
        return ans

if __name__=="__main__":
    n = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    so=Solution()
    a=so.trapRainWater(n)
    print(a)