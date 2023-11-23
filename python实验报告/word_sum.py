import numpy as np
import operator
from time import time
import os

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
steps = []  #保存路径
openlist = []  # open表
closed = []  # closed表


class State:
    def __init__(self, m):
        self.node = m
        self.f = 0
        self.g = 0
        self.h = 0
        self.father = None

# 找到列表中对应元素的下标
def isContained(num_list, num):
    for i in range(len(num_list)):
        if (num.node == num_list[i].node).all():
            return i
    return -1

# 逆序数：所有排列队列在当前位置之前比当前位置上的元素大的计数总和("0"不参与计数)，用于判断奇数列，还是偶数列
def getStatus(numList):
    res = 0
    for i in range(1, len(numList)):
        if numList[i] == 0:
            continue
        for j in range(i):
            if numList[j] > numList[i]:
                res += 1
    return res

 # 判断是否存在解
def existSolution(a_list, b_list):
    a_f = getStatus(a_list)
    b_f = getStatus(b_list)
    print(f"状态1逆序数:{a_f}", f"状态2逆序数:{b_f}")
    if (a_f % 2 == b_f % 2):  ## 逆序数相同，有解
        return True
    return False

# 启发函数
def h(s):
    a = 0
    for i in range(len(s.node)):
        for j in range(len(s.node[i])):
            if s.node[i][j] != goal.node[i][j]:
                a = a + 1
    return a

# 对节点列表按照估价函数的值的规则排序
def list_sort(l):
    cmp = operator.attrgetter('f')
    l.sort(key=cmp)

counter = 0
counter_all = 1

# A*算法
def A_star(s):
    global openlist, closed ,counter ,counter_all
    openlist = [s]
    while (openlist):
        get = openlist.pop(0)
        counter += 1
        closed.append(get)
        if (get.node == goal.node).all():
            return get
        # 判断此时状态的空格位置(a,b)
        for a in range(len(get.node)):
            for b in range(len(get.node[a])):
                if get.node[a][b] == 0:
                    break
            if get.node[a][b] == 0:
                break
        row, col = len(get.node), len(get.node[0])
        for dir in direction:
            i = a + dir[0]
            j = b + dir[1]
            if 0 <= i < row and 0 <= j < col:
                counter_all += 1
                c = get.node.copy()
                c[a][b] = c[i][j]
                c[i][j] = 0
                if (get.father !=None and (c == get.father.node).all()):
                    continue
                new = State(c)
                new.father = get
                new.g = get.g + 1
                if (isContained(closed, new) == -1):
                    position = isContained(openlist, new)
                    if position != -1:
                        if new.g < openlist[position].g:
                            openlist.pop(position)
                            new.h = h(new)
                            new.f = new.g + new.h
                            openlist.append(new)
                    else:
                        new.h = h(new)
                        new.f = new.g + new.h
                        openlist.append(new)
        list_sort(openlist)

# 递归打印路径
def getpath(f):
    global steps
    if f is None:
        return
    getpath(f.father)
    steps.append(f.node)

O, A, B = None, None, None
with open("input.txt", "a", encoding='utf-8') as f:
    f.close()
with open("input.txt", mode="r", encoding='utf-8') as f:
    O = int(f.readline().strip())
    A = [int(i) for i in f.readline().strip().split(",")]
    B = [int(i) for i in f.readline().strip().split(",")]
print(f"矩阵的规模:{O}",f"初始状态{A}", f"目标状态{B}")


if existSolution(A, B):
    z = 0
    M = np.zeros((O, O))
    N = np.zeros((O, O))
    for i in range(O):
        for j in range(O):
            M[i][j] = A[z]
            N[i][j] = B[z]
            z = z + 1
    init = State(M)
    goal = State(N)
    time1 = time()
    final = A_star(init)
    if final:
        print("有解，解为：")
        getpath(final)
        for i, item in enumerate(steps):
            print(f"*****第{i}步*****")
            print(item)
        print("总共考察了%d个节点"%counter)
        print(f"该树已生成的节点数为{counter_all}")
        print(f"总用时为{time()-time1}s")
    else:
        print("无解")
else:
    print("该八数码问题没有解，请重新选择！")
