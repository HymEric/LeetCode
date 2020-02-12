# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 0029 11:24
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 417.py
# @Software: PyCharm
"""
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

 

提示：

输出坐标的顺序不重要
m 和 n 都小于150
 

示例：

 

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def __init__(self):
        self.result_all=None
        # move up, right, down and left
        self.directs=[(-1,0),(0,1),(1,0),(0,-1)]
        self.m=0
        self.n=0
        # denote it can move to pacific ocean
        self.po=None
        # denote it can move to atlantic ocean
        self.ao=None
        self.visited=None

    def pacificAtlantic(self, matrix: list) -> list:
        # init
        self.result_all=[]
        self.m=len(matrix)
        if self.m==0:
            return self.result_all
        self.n=len(matrix[0])
        self.ao=[[0]*self.n for _ in range(self.m)]
        self.po = [[0] * self.n for _ in range(self.m)]
        self.visited = [[0] * self.n for _ in range(self.m)]

        # it is hard to solve it by top-dowm moving, so we use bottom-up moving
        # moving from up: pacific ocean
        for i in range(0,1):
            for j in range(self.n):
                self.dfs(matrix,i,j,True)
        # moving from left: pacific ocean
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(0,1):
                self.dfs(matrix,i,j,True)
        # moving from bottom: atlantic ocean
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m-1,self.m):
            for j in range(self.n):
                self.dfs(matrix,i,j,False)
        # movinig from right: atlantic ocean
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n-1,self.n):
                self.dfs(matrix,i,j,False)
        for i in range(self.m):
            for j in range(self.n):
                if self.po[i][j] ==1 and self.ao[i][j]==1:
                    self.result_all.append((i,j))
        return self.result_all
    def dfs(self,matrix,x,y,flag):
        if self.visited[x][y]==1:
            return
        self.visited[x][y]=1
        if flag:
            # pacific ocean
            self.po[x][y]=1
        else:
            # atlantic ocean
            self.ao[x][y]=1
        for i in range(4):
            newx=x+self.directs[i][0]
            newy=y+self.directs[i][1]
            if not self.in_area(newx,newy):
                continue
            if matrix[x][y]>matrix[newx][newy]:
                continue
            self.dfs(matrix,newx,newy,flag)
        return

    def in_area(self,x,y):
        return 0<=x<self.m and 0<=y<self.n

if __name__=="__main__":
    # s=[[1,2,2,3,5],
    #    [3,2,3,4,4],
    #    [2,4,5,3,1],
    #    [6,7,1,4,5],
    #    [5,1,1,2,4]]
    s=[[1,1],[1,1],[1,1]]
    so=Solution()
    a=so.pacificAtlantic(s)
    print(a)
