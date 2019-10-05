# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 0005 8:49
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 119.py
# @Software: PyCharm

class Solution:
    def getRow(self, rowIndex: int) -> list:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        out=[[1],[1,1]]
        for i in range(2,rowIndex+1,1):
            inside=[]
            for j in range(i+1):
                if j ==0 or j ==i:
                    inside.append(1)
                else:
                    inside.append(out[i-1][j-1]+out[i-1][j])
            out.append(inside)
        return out[-1]

    def getRow2(self, rowIndex: int) -> list:
        if rowIndex<0:
            return None
        temp=[1]
        for i in range(1,rowIndex+1,1):
            temp.insert(0,0)
            for j in range(i):
                temp[j]=temp[j]+temp[j+1]
        return temp


if __name__=="__main__":
    numRows=3
    so=Solution()
    a=so.getRow2(numRows)
    print(a)
