# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 0006 12:37
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 401.py
# @Software: PyCharm
"""
二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。



例如，上面的二进制手表读取 “3:25”。

给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

案例:

输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 

注意事项:

输出的顺序没有要求。
小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-watch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def readBinaryWatch(self, num: int) -> list:
        res=[]
        for h in range(12):
            for m in range(60):
                if (bin(h)+bin(m)).count('1')==num:
                    res.append('{}:{:02d}'.format(h,m))
        return res
    def __init__(self):
        self.result_all=None
        self.nums=[1,2,4,8,1,2,4,8,16,32]
        self.visited=None

    def readBinaryWatch2(self, num: int) -> list:
        self.result_all=[]
        self.visited=[0 for _ in range(len(self.nums))]
        self.dfs(num,0,0)
        return self.result_all
    def dfs(self,num:int,step:int,start:int):
        # step 的数值表示目前亮的灯数量，也就是1的数量
        # 如果亮的等的数量和我们的目标已经一样了
        if step==num:
            self.result_all.append(self.handle_date(self.visited))
            return
        for i in range(start,len(self.nums)):
            self.visited[i]=1
            if not self.is_valid(self.visited):
                self.visited[i]=0
                continue
            self.dfs(num,step+1,i+1)
            self.visited[i]=0
        return
    def is_valid(self,visited:list):
        sum_h=0
        sum_m=0
        for i in range(len(visited)):
            if visited[i]==0:
                continue
            if i<4:
                sum_h+=self.nums[i]
            else:
                sum_m+=self.nums[i]
        return 0<=sum_h<=11 and 0<=sum_m<=59
    def handle_date(self,visited:list):
        sum_h=0
        sum_m=0
        for i in range(len(visited)):
            if visited[i]==0:
                continue
            if i <4:
                sum_h+=self.nums[i]
            else:
                sum_m+=self.nums[i]
        result=""+str(sum_h)+":"
        if sum_m<10:
            result+="0"+str(sum_m)
        else:
            result+=str(sum_m)
        return result



if __name__=="__main__":
    n = 0
    so=Solution()
    a=so.readBinaryWatch2(n)
    print(a)