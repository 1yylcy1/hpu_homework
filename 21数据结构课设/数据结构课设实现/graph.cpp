#include "graph.h"
#include<iostream>
#include<string.h>
using namespace std;
//1.��ʼ���ڽӾ���ͱ߼�����,�ڽӾ��󶼲��ɴ�߼�����Ȩ�ض�����Ϊ0
int Solution ::initial_adj_matrix(Edge*pn,int node,int edge)
{
    for(int i=0;i<node;i++)//i��ʾ��
    {
        for(int j=0;j<node;j++)//j��ʾ��
        {
            if(i==j) adj_matrix[i][j]=0;//������������Ϊ0
            else adj_matrix[i][j]=MaxValue;//��ʼ��������Ϊ���Ȩֵ  
        }
    }
    for(int k;k<edge;k++)
    {
        pn[k].weight=0;//��ÿ���ߵ�Ȩֵ������Ϊ0
    }
    return 0;
}

/*2.����һ����麯����(��㣬�յ㣬Ȩ�أ�������)
���ڼ������������Ƿ����Ҫ��*/
void Solution::check(int i,int j,int w,int node)
{
    while(true)
    {
        if(i<0||j<0||i>node||j>node||w>MaxValue||w<0)//���������쳣�����
        std::cout<<"�����������������"<<endl;
        else return;//���������Ϳ��Է�����
        cin>>i>>j>>w;//�����������ͼ�������
    }
}

//3.�����ڽӾ���,pnΪ�߼��ṹ������ָ��,0��99�Ķ���������
void Solution ::create_adj_matrix(Edge*pn,int edge,int node)
{
	std::cout<<"����������Ȩ�ز�Ϊ0�ıߵ���㣬�յ㣬Ȩ�أ�"<<endl;
    std::cout<<"ֱ������һ��Ȩ��Ϊ0�ıߺ��˳�����"<<endl;
	int a;int b;int c;
    do
    {
        int k=0;
        cout<<"��ܰ��ʾ������ߵĶ����Լ�Ȩ�ر���������������(�������룺1 2 3)"<<endl;
        cin>>a>>b>>c;//������㣬�յ㣬Ȩ��
		check(a,b,c,node);
		if(c==0) break;//��������Ȩ��Ϊ0����ֹͣ
		else{
			 adj_matrix[a][b]=c;//�������Ȩ�ظ�ֵ���ڽӾ���
		adj_matrix[b][a]=c;
		k++;
		}
       
    }while(true);
	
	std::cout<<"�������ڽӾ���Ϊ��"<<endl;
	for(int i =0;i<node;i++)
	{
		for(int j=0;j<node;j++)
		{
			std::cout<<adj_matrix[i][j]<<" ";
		}
		std::cout<<endl;
	}  
}

//4.���߼������С��������(�߼����飬�ߵĸ���)
void Solution ::sort_edge(Edge*pn,int edge)
{
    for(int i=0;i<edge-1;i++)//һ��edge-1��
    {
        for(int k=0;k<edge-i-1;k++)//ÿ�˵ıȽϴ���
        {
            Edge tmp;
            if(pn[k].weight>=pn[k+1].weight)//�ṹ������
            {
                tmp=pn[k];
                pn[k]=pn[k+1];
                pn[k+1]=tmp;
            }
        }
    }
}


//5.prim�㷨
void Solution::adj_prim(int vis[MaxV],int n,int G[MaxV][MaxV],Edge edge_prim[MaxV])
{
    vis[0]=1; int flag=0; int weight=99;int t=0;int weight_sum=0;//(t���ڼ�¼j)
	for(int m=0;m<MaxV;m++)
	{
		weight=99;
		for(int i=0;i<n&&flag<MaxV;i++)//ÿһ�е�
		{
			if(vis[i]==1)//�������Ѿ�����
			{
				for(int j=0;j<n&&flag<=MaxV;j++)//ÿһ�е�
				{
					if (vis[j]==0&&G[i][j]<weight)//������δ����
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
		continue;//˵�����޷�������С������
		else
		{
			vis[t]=1;
			flag++;
		}
	}
	// std::cout<<"Prim�㷨����С������Ϊ��δ����"<<endl;
	// for(int k=0;k<flag;k++)//flag��ʼ��Ϊ1�����Դ�1��ʼ���
	// {
	// 	std::cout<<"("<<edge_prim[k].start_vex<<","<<edge_prim[k].stop_vex<<","<<edge_prim[k].weight<<")"<<" ";
	// 	weight_sum=weight_sum+edge_prim[k].weight;
	// }
	// std::cout<<"prim�㷨������СȨֵ֮��Ϊ"<<weight_sum<<endl;
	sort_edge(edge_prim,flag);
	std::cout<<"Prim�㷨�������۵���ͼΪ������Ȩ������֮��"<<endl;
	weight_sum=0;
	for(int k=0;k<flag;k++)
	{
		std::cout<<"("<<edge_prim[k].start_vex<<","<<edge_prim[k].stop_vex<<","<<edge_prim[k].weight<<")"<<" ";
		weight_sum=weight_sum+edge_prim[k].weight;
	}
	std::cout<<"prim�㷨�������۵�����Ϊ��"<<weight_sum<<endl;
}

//6.ͼ�Ĳ������ݺ���
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
	std::cout<<"����ͼ���ڽӾ���Ϊ��"<<endl;
	for(int i =0;i<7;i++)
	{
		for(int j=0;j<7;j++)
		{
			std::cout<<G[i][j]<<" ";
		}
		std::cout<<endl;
	}   
}
//7.�ж��Ƿ��Ȧ
int Solution::get_end(int vends[], int i)
{
	while (vends[i] != 99)
    i = vends[i];//�����λ�����ˣ����ҵ�����ͬһ����Ӫ��λ��ȥ������ֱ���Ǹ���Ӫû�ˡ�
	//std::cout<<i<<" ";
	return i;
}


//8.KrusKal �㷨
void Solution::adj_KrusKal(Edge* pn,int adj_matrix[MaxV][MaxV],int edge)
{
	//std::cout<<"��ʼִ��KrusKal�㷨"<<endl;
	int i,m,n,p1,p2;
    int length;
    int index = 0;          // rets���������
    int vends[MaxV];     // ���ڱ���"������С������"��ÿ�������ڸ���С���е��յ㡣
	std::fill(vends,vends+MaxV,99);
    Edge rets[MaxV];        // ������飬����kruskal��С�������ı�
    // ���߰���"Ȩ"�Ĵ�С��������(��С����)
    sort_edge(pn, edge);																																	

    for (i=0; i<edge; i++)
    {
		//std::cout<<"("<<pn[i].start_vex<<","<<pn[i].stop_vex<<","<<pn[i].weight<<")"<<" ";// �������·��
        p1 = pn[i].start_vex;   // ��ȡ��i���ߵ�"���"�����
        p2 = pn[i].stop_vex;     // ��ȡ��i���ߵ�"�յ�"�����

        m = get_end(vends, p1);                 // ��ȡp1��"���е���С������"�е��յ�
        n = get_end(vends, p2);                 // ��ȡp2��"���е���С������"�е��յ�
        // ���m!=n����ζ��"��i"��"�Ѿ���ӵ���С�������еĶ���"û���γɻ�·
        if (m != n)
        {
			//std::cout<<"("<<m<<","<<n<<")"<<endl;
            vends[m] = n;                       // ����m��"���е���С������"�е��յ�Ϊn
            rets[index++] = pn[i];           // ������
        }
    }
	
    // ͳ�Ʋ���ӡ"kruskal��С������"����Ϣ
    length = 0;
    for (i = 0; i < index; i++)
        length += rets[i].weight;
    std::cout<<"Kruskal�㷨��������Ϊ"<<length<<endl;
	std::cout<<"KrusKal�㷨�������۵���ͼΪ������Ȩ����С��������"<<endl;
    for (i = 0; i < index; i++)
        std::printf("(%d,%d,%d) ", rets[i].start_vex, rets[i].stop_vex,rets[i].weight);
    std::printf("\n");
}
//9. �����߼�����
void Solution:: create_adj_pn(int G[MaxV][MaxV],int edge_num,int node)
{
	std::cout<<"����������Ȩ�ز�Ϊ0�ıߵ���㣬�յ㣬Ȩ�أ�"<<endl;
    std::cout<<"ֱ������һ��Ȩ��Ϊ0�ıߺ��˳�����"<<endl;
	int flag=0;int a;int b;int c=99;
	for(int i=0;i<edge_num;i++)
	{
		cout<<"��ܰ��ʾ������ߵĶ����Լ�Ȩ�ر���������������(�������룺1 2 3)"<<endl;
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
	std::cout<<"�����ı߼�����Ϊ��"<<endl;
	for(int k=0;k<edge_num;k++)
	{
		std::cout<<"("<<adj_pn[k].start_vex<<","<<adj_pn[k].stop_vex<<","<<adj_pn[k].weight<<")"<<" ";
	}
	std::cout<<endl;  
}
