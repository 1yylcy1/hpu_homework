
//������󶥵���
const int MaxV=7;
const int num=20;

//�������Ȩ��
//Ĭ�����Ȩֵ���޷�������
const int MaxValue=99;

//���ñߵ�����Ԫ������
typedef struct
{
    int start_vex;int stop_vex;//�ߵ������յ�
    int weight;//�ߵ�Ȩ
}Edge;

//����һ��ͼ�ඨ��
class Solution
{
    public://��������
    int edge_num;//����
    int adj_matrix[MaxV][MaxV];//�ڽӾ���
    Edge adj_pn[num];
    int vex=MaxV;//������


    public://��������
    //1.��ʼ���ڽӾ���(�߼������飬������������)
    int initial_adj_matrix(Edge*pn,int node,int edge);

    //2.����һ����麯����(��㣬�յ㣬Ȩ�أ�������)
    void check(int i,int j,int w,int node);
    
    //3.�����ڽӾ���(�߼�����ṹ��ָ�룬������������)
    void create_adj_matrix(Edge*pn,int edge,int node);

    //4.���߼������С��������(�߼����飬�ߵĸ���)
    void sort_edge(Edge*pn,int edge);

    //5.prim �㷨ʵ��ͼ����С������(�������飬���������ڽӾ��󣬱߼�����)
    void adj_prim(int vis[MaxV],int n,int G[MaxV][MaxV],Edge edge_prim[MaxV]);

    //6.�ڽӾ������ͼ���ݺ���(�ڽӾ���)
    void G(int G[MaxV][MaxV],Edge*pn);

    //7.KrusKal �㷨(�߼����飬�ڽӾ��󣬱���)
    void adj_KrusKal(Edge* pn,int adj_matrix[MaxV][MaxV],int edge);

    //8.�ж��Ƿ�Χ��Ȧ(��Ƿ������飬��������)
    int get_end(int vends[], int i);

    //9.�����߼����飨Kruskal��(�ڽӾ��󣬱�����������)
    void create_adj_pn(int G[MaxV][MaxV],int edge_num,int node);
};