# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 0001 10:28
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 310.py
# @Software: PyCharm
"""
对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。

格式

该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。

你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。

示例 1:

输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

输出: [1]
示例 2:

输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

输出: [3, 4]
说明:

 根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
树的高度是指根节点和叶子节点之间最长向下路径上边的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: list) -> list:
        if n==1:
            return [0]
        e=collections.defaultdict(set) # the values of dict is set type
        for i,j in edges: # 统计邻接的点，key是所有的点，values是每个点的邻接点
            e[i]=e[i]|{j}
            e[j]=e[j]|{i}
        q={i for i in e if len(e[i])==1} # 建立初始宽搜索队列，全是只连接一个点的点，也就是度为1
        while n>2:
            t=set() # 临时队列
            for i in q:
                j=e[i].pop() # 把连接点取出
                e[j]-={i} # 链接是双向的，所以要删除关系
                if len(e[j])==1: # 更新后，如果长度为1则要加入下一个轮次
                    t=t|{j}
                n-=1
            q=t
        return list(q)
    def findMinHeightTrees2(self, n: int, edges: list) -> list:
        degree=[0]*n # 节点的度
        result=set([x for x in range(n)]) # 待选节点，初试时全部节点，后面一步一步将叶子节点删除
        if n<=2:
            return list(result)
        graph=[[] for x in range(n)] # 构建地图
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1]+=1
            degree[node2]+=1
        queue= []
        for cur in range(n): #初始入队，将叶子节点入队（度为1的）
            if degree[cur]==1:
                queue.append(cur)
                result.remove(cur) # 入队说明该节点不能成为根节点
        while len(result)>2:
            length=len(queue)
            for _ in range(length):
                cur=queue.pop(0)
                for node in graph[cur]:
                    degree[node]-=1 # 删除连接关系的度
                    if degree[node]==1:
                        queue.append(node)
                        result.remove(node)
        return list(result)



if __name__=="__main__":
    n = 2
    edges = [[0,1]]
    so=Solution()
    a=so.findMinHeightTrees2(n,edges)
    print(a)