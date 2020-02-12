# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 0008 11:23
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : 232.py
# @Software: PyCharm
"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.queue==None:
            self.queue=[]
        self.queue.insert(0,x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.queue)==0 or self.queue==None:
            raise Exception
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.queue)==0 or self.queue==None:
            raise Exception
        return self.queue[len(self.queue)-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.queue==None or len(self.queue)==0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# ["MyQueue","push","push","peek","pop","empty"]
# [[],[1],[2],[],[],[]]
class MyQueue2:
    def __init__(self):
        self.A=[]
        self.B=[]

    def push(self,x:int)->None:
        self.A.append(x)

    def pop(self)->int:
        if self.empty():
            return
        if len(self.B)==0:
            while len(self.A)!=0:
                self.B.append(self.A.pop())
            return self.B.pop()
        else:
            return self.B.pop()

    def peek(self)->int:
        if self.empty():
            return
        if len(self.B)==0:
            while len(self.A)!=0:
                self.B.append(self.A.pop())
            return self.B[-1]
        else:
            return self.B[-1]

    def empty(self)->bool:
        if len(self.A)==0 and len(self.B)==0:
            return True
        else:
            return False
if __name__=="__main__":
    # n =65535
    # so=Solution()
    # a=so.integerReplacement2(n)
    # print(a)
    obj = MyQueue2()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)