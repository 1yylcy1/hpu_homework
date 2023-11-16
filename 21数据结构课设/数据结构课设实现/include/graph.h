
//设置最大顶点数
const int MaxV=7;
const int num=20;

//设置最大权重
//默认最大权值即无法到到达
const int MaxValue=99;

//设置边的数组元素类型
typedef struct
{
    int start_vex;int stop_vex;//边的起点和终点
    int weight;//边的权
}Edge;

//设置一个图类定义
class Solution
{
    public://公有属性
    int edge_num;//边数
    int adj_matrix[MaxV][MaxV];//邻接矩阵
    Edge adj_pn[num];
    int vex=MaxV;//顶点数


    public://公有属性
    //1.初始化邻接矩阵(边集合数组，顶点数，边数)
    int initial_adj_matrix(Edge*pn,int node,int edge);

    //2.创建一个检查函数：(起点，终点，权重，顶点数)
    void check(int i,int j,int w,int node);
    
    //3.创建邻接矩阵(边集数组结构体指针，边数，顶点数)
    void create_adj_matrix(Edge*pn,int edge,int node);

    //4.将边集数组从小到大排序(边集数组，边的个数)
    void sort_edge(Edge*pn,int edge);

    //5.prim 算法实现图的最小生成树(访问数组，顶点数，邻接矩阵，边集数组)
    void adj_prim(int vis[MaxV],int n,int G[MaxV][MaxV],Edge edge_prim[MaxV]);

    //6.邻接矩阵测试图数据函数(邻接矩阵)
    void G(int G[MaxV][MaxV],Edge*pn);

    //7.KrusKal 算法(边集数组，邻接矩阵，边数)
    void adj_KrusKal(Edge* pn,int adj_matrix[MaxV][MaxV],int edge);

    //8.判断是否围成圈(标记访问数组，遍历索引)
    int get_end(int vends[], int i);

    //9.创建边集数组（Kruskal）(邻接矩阵，边数，顶点数)
    void create_adj_pn(int G[MaxV][MaxV],int edge_num,int node);
};