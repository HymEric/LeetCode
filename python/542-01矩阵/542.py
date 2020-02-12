# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 0031 21:26
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 542.py
# @Software: PyCharm
"""
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
注意:

给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def updateMatrix(self, matrix: list) -> list: # BFS
        def count(row_index,col_index,point):
            if point==0:
                return 0
            else:
                que,distance=[(row_index,col_index)],0
                visited=set()
                while que:
                    distance,length=distance+1,len(que)
                    for _ in range(length):
                        newpoint=que.pop()
                        for newx,newy in zip((newpoint[0],newpoint[0],newpoint[0]-1,newpoint[0]+1),
                                             (newpoint[1]-1,newpoint[1]+1,newpoint[1],newpoint[1])):
                            if 0<=newx<len(matrix) and 0<=newy<len(matrix[0]) and (newx,newy) not in visited:
                                if matrix[newx][newy]!=0:
                                    que.insert(0,(newx,newy))
                                    visited.add((newx,newy))
                                else:
                                    return distance
        distance_matrix=[[0 for j in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row_index,row in enumerate(matrix):
            for col_index,point in enumerate(row):
                distance_matrix[row_index][col_index]=count(row_index,col_index,point)
        return distance_matrix

    def updateMatrix2(self, matrix: list) -> list:
        row_len = len(matrix)
        col_len = len(matrix[0])
        for i in range(row_len):
            for j in range(col_len):
                row_, col_ = 10001, 10001
                if matrix[i][j] != 0:
                    if i > 0:
                        row_ = matrix[i - 1][j]
                    if j > 0:
                        col_ = matrix[i][j - 1]
                    matrix[i][j] = min(row_, col_) + 1
        for i in range(row_len-1,-1,-1):
            for j in range(col_len-1,-1,-1):
                row_,col_=10001,10001
                if matrix[i][j]!=0:
                    if i<row_len-1:
                        row_=matrix[i+1][j]
                    if j<col_len-1:
                        col_=matrix[i][j+1]
                    matrix[i][j]=min(matrix[i][j],min(row_,col_)+1)
        return matrix




if __name__=="__main__":
    n=[[0, 0 ,0],
       [0 ,1, 0],
       [1 ,1, 1]]
    so=Solution()
    a=so.updateMatrix2(n)
    print(a)