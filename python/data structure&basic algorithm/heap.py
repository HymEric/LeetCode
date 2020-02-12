# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 0027 15:44
# @Author  : Erichym
# @Email   : 951523291@qq.com
# @File    : heap.py
# @Software: PyCharm
"""
implement max-heap and min-heap with their related operators
并不是排序堆
"""
class Array(object):
    """
    achive an Array by Python list
    """
    def __init__(self,size=32):
        self._size=size
        self._items=[None]*size

    def __getitem__(self, index):
        """
        Get items
        :param index: get a value by index
        :return: value
        """
        return self._items[index]

    def __setitem__(self, index, value):
        """
        set item
        :param index: giving a index you want to set
        :param value: the value want to set
        :return:
        """
        self._items[index]=value

    def __len__(self):
        """
        :return: the length of array
        """
        return self._size

    def clear(self,value=None):
        """
        cllear the Array
        :param value: set all value to None
        :return:
        """
        for i in range(self._size):
            self._items[i]=value

    def __iter__(self):
        for item in self._items:
            yield item

class MaxHeap(object):
    def __init__(self,maxsize=None):
        self.maxsize=maxsize
        self._elements=Array(maxsize)
        self._count=0

    def __len__(self):
        return self._count

    def add(self,value):
        if self._count>=self.maxsize:
            raise Exception('full')
        self._elements[self._count]=value
        self._count+=1
        self._siftup(self._count-1) # keep the features of maxHeap

    def _siftup(self,ndx):
        if ndx>0:
            parent=int((ndx-1)/2)
            if self._elements[ndx]>self._elements[parent]: # if add value>parent value
                self._elements[ndx],self._elements[parent]=self._elements[parent],self._elements[ndx]
                self._siftup(parent) # recursion 递归

    def extract(self):
        if self._count<=0:
            raise Exception('empty')
        value=self._elements[0]
        self._count-=1
        self._elements[0]=self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self,ndx):
        left=2*ndx+1
        right=2*ndx+2
        # which one contains larger value
        largest=ndx
        if (left<self._count and # have left children
                self._elements[left]>=self._elements[largest] and
                self._elements[left]>=self._elements[right]):
            largest=left
        elif (right<self._count and
              self._elements[right]>=self._elements[largest] and
              self._elements[right]>=self._elements[left]):
            largest=right
        if largest!=ndx:
            self._elements[ndx],self._elements[largest]=self._elements[largest],self._elements[ndx]
            self._siftdown(largest)

def test_maxheap():
    # import random
    n=5
    h=MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        # print('i',i)
        # print(h.extract())
        assert i == h.extract()

class MinHeap(object):
    """
    Achieve a minimum heap using list instead of Array created above
    """
    def __init__(self,maxsize=None):
        self.maxsize=maxsize
        self._elements=list([None]*maxsize)
        self._count=0

    def __len__(self):
        return self._count

    def add(self,value):
        """
        add an element to heap while keeping the attribute of heap
        :param value: the value added to the heap
        :return: None
        """
        if self._count>self.maxsize:
            raise Exception("full")
        self._elements[self._count]=value
        self._count+=1
        self._siftup(self._count-1)

    def _siftup(self,index):
        """
        To keep the the attribute of heap unchanged while adding a new value.
        :param index: the index of value you want to swap
        :return: None
        """
        if index >0:
            parent=int((index-1)/2)
            if self._elements[parent]>self._elements[index]:
                self._elements[parent],self._elements[index]=self._elements[index],self._elements[parent]
                self._siftup(parent)

    def extract(self):
        """
        pop and return the value of root
        :return: the value of root
        """
        if self._count<=0:
            raise Exception('The heap is empty!')
        value=self._elements[0]
        self._count-=1
        self._elements[0]=self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self,index):
        """
        to keep the attribute of heap unchanged while pop out the root node.
        :param index: the index of value you want to swap
        :return: None
        """
        if index < self._count:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < self._count and right < self._count \
                and self._elements[left] <= self._elements[right] \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)
            elif left < self._count and right < self._count \
                and self._elements[left] >= self._elements[right] \
                and self._elements[right] <= self._elements[index]:
                self._elements[right], self._elements[index] = self._elements[index], self._elements[right]
                self._siftdown(left)

            if left < self._count and right > self._count \
                and self._elements[left] <= self._elements[index]:
                self._elements[left], self._elements[index] = self._elements[index], self._elements[left]
                self._siftdown(left)

def test_minheap():
    n = 5
    h = MinHeap(5)
    # for i in range(n):
    #     h.add(i)
    # h.add(0)
    # h.add(1)
    # h.add(2)
    # h.add(3)
    # h.add(4)
    h.add(14)
    h.add(10)
    h.add(9)
    h.add(45)
    h.add(6)
    for i in range(5):
        print(h.extract())
        # assert i == h.extract()
    # print(h.extract())
    # print(h.extract())

if __name__=="__main__":
    test_minheap()