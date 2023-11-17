import random
import string

def Eval(a1,a2):        #适应度函数
    a = 1 / (a1 * a1 + a2 * a2 + 1)
    return a

def init(size, population, x1, x2, a):  #初始化种群
    sum = (x2 - x1) / a
    a = 0
    while(pow(2, a) - 1 < sum):    #需要多长的代码
        a=a+1
    for i in range (0, size):    #生成size个初始个体
        x1 = random.randint(0, pow(2, a) - 1)
        x2 = random.randint(0, pow(2, a) - 1)
        s1 = bin(x1).replace('0b','')
        s2 = bin(x2).replace('0b','')
        list1 = list(s1)
        list2 = list(s2)
        len1 = len(list1)
        len2 = len(list2)
        while(len1 < a):
            list1.insert(0,'0')
            len1=len1 + 1
        while(len2 < a):
            list2.insert(0,'0')
            len2=len2 + 1
        s1 = ''.join(list1)
        s2 = ''.join(list2)
        s = s1 + s2
        population.append(s)
    return a

def bit_solve(s):   #二进制化为整数
    l = len(s)
    s = s[::-1]
    ans=0
    for i in range(0,l):
        ans = ans + pow(2,i) * (int)(s[i])
    return ans

def fit_solve(population, fitness, size, n, dt, x1):     #求种群适应度
    for i in range(0, size):
        s1=""
        s2=""
        for j in range(0, n):
            s1+=population[i][j]
        for j in range(n, 2 * n):
            s2+=population[i][j]
        a1 = bit_solve(s1) * dt + x1
        a2 = bit_solve(s2) * dt + x1
        a = Eval(a1,a2)
        fitness.append(a)

def choose(population, new_pop, fitness, size):        #轮盘赌选择
    F = 0
    roulette = []
    p = 0
    for i in range(0, size):
        F = F + fitness[i]
    for i in range(0, size):
        p = p + fitness[i] / F
        roulette.append(p)
    for i in range(0, size):
        p = random.uniform(0,1)
        for j in range(0, size):
            if(roulette[j] >= p):
                new_pop.append(population[j])

def inheritance_solve(population, size, inheritance, n):       #遗传
    s1 = ""
    s2 = ""
    size = int(size / 2)
    for i in range(0, size):
        p = random.uniform(0,1)
        if(p < inheritance):
            a = random.randint(0, n-1)
            for j in range(0, a):
                s1 += population[2 * i][j]
                s2 += population[2 * i + 1][j]
            for j in range(a, n):
                s1 += population[2 * i + 1][j]
                s2 += population[2 * i][j]

def variation_solve(population, size, variation, n):       #变异
    for i in range(0, size):
        for j in range(0, n):
            p = random.uniform(0,1)
            if(p < variation):
                if(population[i][j]=='0'):
                    list1 = list(population[i])
                    list1[j] = '1'
                    population[i]=''.join(list1)
                else:
                    list1 = list(population[i])
                    list1[j] = '0'
                    population[i] = ''.join(list1)

def main():
    #求解函数方程y=1/(x1*x1+x2*x2+1)
    #-5<=x1,x2<=5，精度为0.0001
    #采用二进制编码，单点交叉，单点变异，交叉概率0.8，变异概率0.1，进化代数100
    size = 26           #种群规模
    inheritance = 0.8   #遗传概率
    variation = 0.1     #变异概率
    population = []     #种群
    x1 = -5             #范围
    x2 = 5
    a = 0.0001          #精度
    cnt = 100            #进化代数
    str=""              #最优染色体
    ans=0               #最大适应度
    n = init(size, population, x1, x2, a)   #初始化种群
    dt = (x2 - x1) / (pow(2, n) - 1)
    while(cnt):
        new_pop = []
        cnt=cnt-1
        fitness = []
        fit_solve(population,fitness,size,n,dt,x1)
        for i in range(0,size):
            if(fitness[i]>ans):
                ans = fitness[i]
                str = population[i]
        choose(population,new_pop,fitness,size)
        population = new_pop
        inheritance_solve(population,size,inheritance,2*n)
        variation_solve(population,size,variation,2*n)
    fitness = []
    fit_solve(population,fitness,size,n,dt,x1)
    for i in range(0, size):
        if (fitness[i] > ans):
            ans = fitness[i]
            str = population[i]
    print('遗传算法得到的最大适应度为：{:.2f} 其基因型为：'.format(ans),str)
    s1 = ""
    s2 = ""
    for j in range(0, n):
        s1 += str[j]
    for j in range(n, 2 * n):
        s2 += str[j]
    a1 = bit_solve(s1) * dt + x1
    a2 = bit_solve(s2) * dt + x1
    a = Eval(a1, a2)
    print('x1 = {:.2f}'.format(a1)," x2 = {:.2f}".format(a2)," y = {:.2f}".format(a))


main()
