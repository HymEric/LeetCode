# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 0003 9:20
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 609.py
# @Software: PyCharm
import collections

class Solution:
    def findDuplicate(self, paths: list) -> list:
        n=len(paths)
        full_paths=[]
        dict_content=collections.defaultdict(list)
        for i in range(n):
            path=paths[i]
            path_split=path.split(' ')
            length=len(path_split)
            head=path_split[0]
            for j in range(1,length,1):
                full_paths.append(head+'/'+path_split[j])
        # print(full_paths)
        for i in range(len(full_paths)):
            cont_key=full_paths[i].split('(')[1][:-1] # for key, it slao can omit the [:-1
            dict_content[cont_key]+=[full_paths[i].split('(')[0]]
        return list(filter(lambda s:len(s)>1,dict_content.values()))
    def findDuplicate2(self, paths: list) -> list:
        d=collections.defaultdict(list)
        for path in paths:
            doc=path.split(' ')
            for file in doc[1:]:
                name,content=file.split("(")
                # print(content)
                d[hash(content)]+=[doc[0]+'/'+name] # hash to save space
        return list(filter(lambda s: len(s)>1,d.values()))


if __name__=="__main__":
    l=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    so=Solution()
    a=so.findDuplicate2(l)
    print(a)