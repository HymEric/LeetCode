# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 0003 21:39
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 118.py
# @Software: PyCharm

class Solution:
    def generate(self, numRows: int) -> list:
        if numRows==0:
            return []
        out=[]
        for i in range(numRows):
            if i ==0:
                inside=[1]
                out.append(inside)
            else:
                inside=[]
                for j in range(i+1):
                    # print('ee',i)
                    if j==0 or j==i:
                        # print("tt",j)
                        inside.append(1)
                    else:
                        # print('uu',j)
                        inside.append(out[i-1][j-1]+out[i-1][j])
                out.append(inside)
        return out


if __name__=="__main__":
    numRows=6
    so=Solution()
    a=so.generate(numRows)
    print(a)
