# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 0031 20:07
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 313.py
# @Software: PyCharm
"""
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        uglies_dp=[1] # super ugly
        primes_len=len(primes)
        primes_ugly_index=[0]*primes_len # the index in uglies_dp 第一个位置的元素表明primes的质因数在uglies_dp中的位置
        while(n>1): # 第一个质因数是1，再添加n-1的质因数
            # 求质数列表中的每个质数和各自指针对应的超级丑数的乘积的最小值
            min_=min([uglies_dp[primes_ugly_index[i]]*primes[i] for i in range(primes_len)])
            for j in range(primes_len):
                # 若最小值等于该质数乘以uglies_dp[primes_ugly_index[j]]*primes[j]（第i个质数的指针所对应的超级丑数）
                # 则对应指针往后移动一步，i+1
                if min_==uglies_dp[primes_ugly_index[j]]*primes[j]:
                    primes_ugly_index[j]+=1
            n-=1
            uglies_dp.append(min_)
        return uglies_dp[-1]
    def nthSuperUglyNumber2(self, n: int, primes: list) -> int:
        import heapq
        heap=[1]
        n-=1
        while(n):
            temp=heapq.heappop(heap)
            while heap and temp==heap[0]:
                temp=heapq.heappop(heap)
            for j in range(len(primes)):
                heapq.heappush(heap,primes[j]*temp)
            n-=1
        return heapq.heappop(heap)


if __name__=="__main__":
    n = 12
    primes = [2, 7, 13, 19]
    so=Solution()
    a=so.nthSuperUglyNumber2(n,primes)
    print(a)