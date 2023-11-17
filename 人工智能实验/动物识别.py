def init(key1,key2,value1,value2,list):
    print("      构建规则库：")
    print("构建间接数据库，输入0结束：")
    while(1):
        str = input("请输入条件，以空格隔开：")
        if(str=='0'):
            break
        a = str.split()
        b = input("请输入结果：")
        l = len(a)
        for i in range(0,l):
            list.append(a[i])
        key1.append(a)
        value1.append(b)
    print("构建直接数据库，输入0结束：")
    while(1):
        str = input("请输入条件，以空格隔开：")
        if (str == '0'):
            break
        a = str.split()
        b = input("请输入结果：")
        l = len(a)
        for i in range(0, l):
            list.append(a[i])
        key2.append(a)
        value2.append(b)
    print("初始化完毕！")
    return 1

def check(key1,key2,value1,value2,list):
    mp = {}
    l = len(list)
    for i in range(0,l):
        mp[list[i]]=0
    str = input("请输入动物主要特征(使用空格分开)：")
    list1 = str.split()
    l1 = len(list1)
    for i in range(0,l1):
        mp[list1[i]]=1
    len1=len(key1)
    vis = [0]*1000
    while(1):
        v=0
        for i in range(0,len1):
            if(vis[i]):
                continue
            list1 = key1[i]
            len11 = len(list1)
            flag = 1
            for j in range(0,len11):
                if(mp[list1[j]]==0):
                    flag = 0
                    break
            if(flag):
                mp[value1[i]]=1
                vis[i]=1
                v=1
        if(v==0):
            break
    len1=len(key2)
    for i in range(0, len1):
        list1 = key2[i]
        len11 = len(list1)
        flag = 1
        for j in range(0, len11):
            if (mp[list1[j]] == 0):
                flag = 0
                break
        if (flag):
            return value2[i]
    s = '无法识别'
    return s

def solve(key1,key2,value1,value2,list):
    while(1):
        flag = int(input("请输入接下来操作(1.添加间接数据库 2.添加直接数据库 3.查询动物 0.结束操作）："))
        if(flag==1):
            str = input("请输入条件，以空格隔开：")
            a = str.split()
            b = input("请输入结果：")
            l = len(a)
            for i in range(0, l):
                list.append(a[i])
            key1.append(a)
            value1.append(b)
        elif(flag==2):
            str = input("请输入条件，以空格隔开：")
            a = str.split()
            b = input("请输入结果：")
            l = len(a)
            for i in range(0, l):
                list.append(a[i])
            key2.append(a)
            value2.append(b)
        elif(flag==3):
            str = check(key1,key2,value1,value2,list)
            print("该动物：",str)
        elif(flag==0):
            break

def main():
    list = []
    key1 = []
    key2 = []
    value1 = []
    value2 = []
    init(key1,key2,value1,value2,list)
    solve(key1,key2,value1,value2,list)
main()