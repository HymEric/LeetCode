# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 0015 16:21
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 520.py
# @Software: PyCharm
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if 97<=ord(word[0])<=122:
            for i in range(1,len(word),1):
                if ord(word[i])>122 or ord(word[i])<97:
                    return False
            return True
        # first alpha is capital
        elif len(word)>1:
            if 65 <= ord(word[1]) <= 90:
                for i in range(2, len(word), 1):
                    if ord(word[i]) > 90 or ord(word[i]) < 65:
                        return False
                return True
            if 97 <= ord(word[1]) <= 122:
                for i in range(1, len(word), 1):
                    if ord(word[i]) > 122 or ord(word[i]) < 97:
                        return False
                return True
        else:
            return True

    def detectCapitalUse2(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
if __name__=="__main__":
    word="G"
    so=Solution()
    a=so.detectCapitalUse2(word)
    print(a)
