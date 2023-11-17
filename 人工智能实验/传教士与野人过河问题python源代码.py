
import operator

__metaclass__ = type
 
M = int(input("请输入传教士的人数："))  # 传教士
C = int(input("请输入野人的人数:"))  # 野人
K = int(input("请输入船的最大容量："))
# 每船乘坐人数
child = []  # child用来存所有的拓展节点
open_list = []  # open表
closed_list = []  # closed表
 
 
class State:
    def __init__(self, m, c, b):
        self.m = m  #左岸传教士数量
        self.c = c  #左岸野人数量
        self.b = b  # b = 1: 船在左岸；b = 0: 船在右岸
        self.g = 0
        self.f = 0  #f = g+h
        self.father = None
        self.node = [m, c, b]
 
init = State(M, C, 1)  # 初始节点
goal = State(0, 0, 0)  # 目标
 
#0 ≤ m ≤ 3,0 ≤ c ≤ 3, b ∈ {0,1}, 左岸m > c(m 不为 0 时), 右岸3-m > 3-c(m 不为 3 时)
def safe(s):
    if s.m > M or s.m < 0 or s.c > C or s.c < 0 or (s.m != 0 and s.m < s.c) or (s.m != M and M - s.m < C - s.c):
        return False
    else:
        return True
 
 
# 启发函数
def h(s):
    return s.m + s.c - K * s.b
    # return M - s.m + C - s.c
 
def equal(a, b):
    if a.node == b.node:
        return 1,b
    else:
        return 0,b
 
# 判断当前状态与父状态是否一致
def back(new, s):
    if s.father is None:
        return False
    #判断当前状态与祖先状态是否一致
    c=b=s.father
    while(1):
        a,c=equal(new, b)
        if a:
            return True
        b=c.father
        if b is None:
            return False
# 将open_list以f值进行排序
def open_sort(l):
    the_key = operator.attrgetter('f')  # 指定属性排序的key
    l.sort(key=the_key)
 
 
# 扩展节点时在open表和closed表中找原来是否存在相同mcb属性的节点
def in_list(new, l):
    for item in l:
        if new.node == item.node:
            return True, item
    return False, None
 
 
def A_star(s):
    A=[]
    global open_list, closed_list
    open_list = [s]
    closed_list = []
    #print(len(open_list))
    # print （'closed list:'）  # 选择打印open表或closed表变化过程
    #print(s.node)
    #a=1
    while(1):  # open表非空
        #get = open_list[0]  # 取出open表第一个元素get
        for i in open_list:
            if i.node == goal.node:  # 判断是否为目标节点
                A.append(i)
                open_list.remove(i)
        if not(open_list):
            break
        get=open_list[0]
        open_list.remove(get)  # 将get从open表移出
        closed_list.append(get)  # 将get加入closed表
 
        # 以下得到一个get的新子节点new并考虑是否放入openlist
        for i in range(M+1):  # 上船传教士
            for j in range(C+1):  # 上船野人
                # 船上非法情况
                if i + j == 0 or i + j > K or (i != 0 and i < j):
                    continue
                #a=a+1
                if get.b == 1:  # 当前船在左岸，下一状态统计船在右岸的情况
                    new = State(get.m - i, get.c - j, 0)
                    child.append(new)
                    #print(1)
                else:  # 当前船在右岸，下一状态统计船在左岸的情况
                    new = State(get.m + i, get.c + j, 1)
                    child.append(new)
                    #print(2)
                #优先级：not>and>ture。如果状态不安全或者要拓展的节点与当前节点的父节点状态一致。
                if not safe(new) or back(new, get):  # 状态非法或new折返了
                    child.pop()
                #如果要拓展的节点满足以上情况，将它的父亲设为当前节点，计算f，并对open_list排序
                else:
                    new.father = get
                    new.g = get.g + 1  #与起点的距离
                    new.f = get.g + h(get)  # f = g + h

                    open_list.append(new)
                    #print(len(open_list))
                    open_sort(open_list)
        # 打印open表或closed表
        #for o in open_list:
        # for o in closed_list:
            #print(o)
            #print(o.node)
           # print(o.father)
        #print(a)
    return(A)
                        
 
# 递归打印路径
def printPath(f):
    if f is None:
        return
    printPath(f.father)
    #注意print()语句放在递归调用前和递归调用后的区别。放在后实现了倒叙输出
    print(f.node )
 
 
if __name__ == '__main__':
    print ('有%d个传教士，%d个野人，船容量:%d' % (M, C, K))
    final = A_star(init)
    print("有{}种方案".format(len(final)))
    if final:
        for i in(final):
            print ('有解，解为：')
            printPath(i)
    else:
        print ('无解！')