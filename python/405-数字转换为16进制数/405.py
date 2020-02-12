# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 0006 11:44
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 405.py
# @Software: PyCharm
"""
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：

输入:
26

输出:
"1a"
示例 2：

输入:
-1

输出:
"ffffffff"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    # def toHex(self, num: int) -> str:
    #     hex_dict={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
    #               10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    #     def toH(num:int): # num>0
    #         res=''
    #         while num:
    #             num,i=divmod(num,16)
    #             res=res+hex_dict[i]
    #         return res[::-1]
    #     if num ==0:
    #         return '0'
    #     elif num>0:
    #         return toH(num)
    #     else:
    #         num_=-num
    #         tmp=toH(num_)
    def toHex2(self, num: int) -> str:
        num=num&0xffffffff
        mask=0b1111
        res=''
        s='0123456789abcdef'
        while num>0:
            tmp=num&mask
            res=res+s[tmp]
            num>>=4
        return res[::-1] if res else '0'

if __name__=="__main__":
    n = -1
    so=Solution()
    a=so.toHex2(n)
    print(a)