#include "graph.h"
#include<iostream>
#include<string.h>
using namespace std;
//1.初始化邻接矩阵和边集数组,邻接矩阵都不可达，边集数组权重都设置为0
int Solution ::initial_adj_matrix(Edge*pn,int node,int edge)
{
    for(int i=0;i<node;i++)//i表示行
    {
        for(int j=0;j<node;j++)//j表示列
        {
            if(i==j) adj_matrix[i][j]=0;//自身到自身设置为0
            else adj_matrix[i][j]=MaxValue;//初始化均设置为最大权值  
        }
    }
    for(int k;k<edge;k++)
    {
        pn[k].weight=0;//将每条边的权值都设置为0
    }
    return 0;
}

/*2.创建一个检查函数：(起点，终点，权重，顶点数)
用于检查输入的数字是否符合要求*/
void Solution::check(int i,int j,int w,int node)
{
    while(true)
    {
        if(i<0||j<0||i>node||j>node||w>MaxValue||w<0)//设置数据异常的情况
        std::cout<<"输入错误，请重新输入"<<endl;
        else return;//数据正常就可以返回了
        cin>>i>>j>>w;//数据输入错误就继续输入
    }
}

//3.创建邻接矩阵,pn为边集结构体数组指针,0和99的都不用输入
void Solution ::create_adj_matrix(Edge*pn,int edge,int node)
{
	std::cout<<"请依次输入权重不为0的边的起点，终点，权重："<<endl;
    std::cout<<"直到输入一条权重为0的边后退出输入"<<endl;
	int a;int b;int c;
    do
    {
        int k=0;
        cout<<"温馨提示：输入边的顶点以及权重必须以数字命名：(样例输入：1 2 3)"<<endl;
        cin>>a>>b>>c;//输入起点，终点，权重
		check(a,b,c,node);
		if(c==0) break;//如果输入的权重为0，则停止
		else{
			 adj_matrix[a][b]=c;//将输入的权重赋值给邻接矩阵
		adj_matrix[b][a]=c;
		k++;
		}
       
    }while(true);
	
	std::cout<<"创建的邻接矩阵为："<<endl;
	for(int i =0;i<node;i++)
	{
		for(int j=0;j<node;j++)
		{
			std::cout<<adj_matrix[i][j]<<" ";
		}
		std::cout<<endl;
	}  
}

//4.将边集数组从小到大排序(边集数组，边的个数)
void Solution ::sort_edge(Edge*pn,int edge)
{
    for(int i=0;i<edge-1;i++)//一共edge-1躺
    {
        for(int k=0;k<edge-i-1;k++)//每趟的比较次数
        {
            Edge tmp;
            if(pn[k].weight>=pn[k+1].weight)//结构体排序
            {
                tmp=pn[k];
                pn[k]=pn[k+1];
                pn[k+1]=tmp;
            }
        }
    }
}


//5.prim算法
void Solution::adj_prim(int vis[MaxV],int n,int G[MaxV][MaxV],Edge edge_prim[MaxV])
{
    vis[0]=1; int flag=0; int weight=99;int t=0;int weight_sum=0;//(t用于记录j)
	for(int m=0;m<MaxV;m++)
	{
		weight=99;
		for(int i=0;i<n&&flag<MaxV;i++)//每一行的
		{
			if(vis[i]==1)//代表其已经访问
			{
				for(int j=0;j<n&&flag<=MaxV;j++)//每一列的
				{
					if (vis[j]==0&&G[i][j]<weight)//代表其未访问
					{
						edge_prim[flag].weight=G[i][j];
						edge_prim[flag].start_vex=i;
						edge_prim[flag].stop_vex=j;
						t=j;
						weight=G[i][j];	
					}
				}
			}
			else continue;
		
		}
	if(weight==99) 
		continue;//说明它无法构成最小生成树
		else
		{
			vis[t]=1;
			flag++;
		}
	}
	// std::cout<<"Prim算法的最小生成树为（未排序）"<<endl;
	// for(int k=0;k<flag;k++)//flag初始化为1，所以从1开始输出
	// {
	// 	std::cout<<"("<<edge_prim[k].start_vex<<","<<edge_prim[k].stop_vex<<","<<edge_prim[k].weight<<")"<<" ";
	// 	weight_sum=weight_sum+edge_prim[k].weight;
	// }
	// std::cout<<"prim算法所得最小权值之和为"<<weight_sum<<endl;
	sort_edge(edge_prim,flag);
	std::cout<<"Prim算法的最低造价电网图为（按“权”排序之后）"<<endl;
	weight_sum=0;
	for(int k=0;k<flag;k++)
	{
		std::cout<<"("<<edge_prim[k].start_vex<<","<<edge_prim[k].stop_vex<<","<<edge_prim[k].weight<<")"<<" ";
		weight_sum=weight_sum+edge_prim[k].weight;
	}
	std::cout<<"prim算法的最低造价电网和为："<<weight_sum<<endl;
}

//6.图的测试数据函数
void Solution ::G(int G[MaxV][MaxV],Edge*pn)
{
    fill(G[0],G[0]+7*7,99);
	G[1][0]=50;G[0][1]=50;pn[0].start_vex=1;pn[0].stop_vex=0;pn[0].weight=50;
	G[2][0]=60;G[0][2]=60;pn[1].start_vex=2;pn[1].stop_vex=0;pn[1].weight=60;
	G[3][1]=65;G[1][3]=65;pn[2].start_vex=3;pn[2].stop_vex=1;pn[2].weight=65;
	G[3][2]=52;G[2][3]=52;pn[3].start_vex=3;pn[3].stop_vex=2;pn[3].weight=52;
	G[4][1]=40;G[1][4]=40;pn[4].start_vex=4;pn[4].stop_vex=1;pn[4].weight=40;
	G[4][3]=50;G[3][4]=50;pn[5].start_vex=4;pn[5].stop_vex=3;pn[5].weight=50;
	G[5][3]=30;G[3][5]=30;pn[6].start_vex=5;pn[6].stop_vex=3;pn[6].weight=30;
	G[5][4]=70;G[4][5]=70;pn[7].start_vex=5;pn[7].stop_vex=4;pn[7].weight=70;
	G[6][2]=45;G[2][6]=45;pn[8].start_vex=6;pn[8].stop_vex=2;pn[8].weight=45;
	G[6][3]=42;G[3][6]=42;pn[9].start_vex=6;pn[9].stop_vex=3;pn[9].weight=42;
	for(int i =0;i<7;i++)
	{
		for(int j=0;j<7;j++)
		{
			if(i==j)
			G[i][j]=0;
			else continue;
		}
	}
	std::cout<<"测试图的邻接矩阵为："<<endl;
	for(int i =0;i<7;i++)
	{
		for(int j=0;j<7;j++)
		{
			std::cout<<G[i][j]<<" ";
		}
		std::cout<<endl;
	}   
}
//7.判断是否成圈
int Solution::get_end(int vends[], int i)
{
	while (vends[i] != 99)
    i = vends[i];//如果该位置有人，则找到与它同一个阵营的位置去看看，直到那个阵营没人。
	//std::cout<<i<<" ";
	return i;
}


//8.KrusKal 算法
void Solution::adj_KrusKal(Edge* pn,int adj_matrix[MaxV][MaxV],int edge)
{
	//std::cout<<"开始执行KrusKal算法"<<endl;
	int i,m,n,p1,p2;
    int length;
    int index = 0;          // rets数组的索引
    int vends[MaxV];     // 用于保存"已有最小生成树"中每个顶点在该最小树中的终点。
	std::fill(vends,vends+MaxV,99);
    Edge rets[MaxV];        // 结果数组，保存kruskal最小生成树的边
    // 将边按照"权"的大小进行排序(从小到大)
    sort_edge(pn, edge);																																	

    for (i=0; i<edge; i++)
    {
		//std::cout<<"("<<pn[i].start_vex<<","<<pn[i].stop_vex<<","<<pn[i].weight<<")"<<" ";// 输出所有路径
        p1 = pn[i].start_vex;   // 获取第i条边的"起点"的序号
        p2 = pn[i].stop_vex;     // 获取第i条边的"终点"的序号

        m = get_end(vends, p1);                 // 获取p1在"已有的最小生成树"中的终点
        n = get_end(vends, p2);                 // 获取p2在"已有的最小生成树"中的终点
        // 如果m!=n，意味着"边i"与"已经添加到最小生成树中的顶点"没有形成环路
        if (m != n)
        {
			//std::cout<<"("<<m<<","<<n<<")"<<endl;
            vends[m] = n;                       // 设置m在"已有的最小生成树"中的终点为n
            rets[index++] = pn[i];           // 保存结果
        }
    }
	
    // 统计并打印"kruskal最小生成树"的信息
    length = 0;
    for (i = 0; i < index; i++)
        length += rets[i].weight;
    std::cout<<"Kruskal算法的最低造价为"<<length<<endl;
	std::cout<<"KrusKal算法的最低造价电网图为（按“权”从小到大排序）"<<endl;
    for (i = 0; i < index; i++)
        std::printf("(%d,%d,%d) ", rets[i].start_vex, rets[i].stop_vex,rets[i].weight);
    std::printf("\n");
}
//9. 创建边集数组
void Solution:: create_adj_pn(int G[MaxV][MaxV],int edge_num,int node)
{
	std::cout<<"请依次输入权重不为0的边的起点，终点，权重："<<endl;
    std::cout<<"直到输入一条权重为0的边后退出输入"<<endl;
	int flag=0;int a;int b;int c=99;
	for(int i=0;i<edge_num;i++)
	{
		cout<<"温馨提示：输入边的顶点以及权重必须以数字命名：(样例输入：1 2 3)"<<endl;
		cin>>a>>b>>c;
		check(a,b,c,node);
		if(c==0){break;}
		else
		{
			adj_pn[flag].start_vex=a;
			adj_pn[flag].stop_vex=b;
			adj_pn[flag].weight=c;
			flag++;
		}
		
	}
	std::cout<<"创建的边集数组为："<<endl;
	for(int k=0;k<edge_num;k++)
	{
		std::cout<<"("<<adj_pn[k].start_vex<<","<<adj_pn[k].stop_vex<<","<<adj_pn[k].weight<<")"<<" ";
	}
	std::cout<<endl;  
}
