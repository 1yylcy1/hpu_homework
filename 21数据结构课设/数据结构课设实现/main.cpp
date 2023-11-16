#include"graph.cpp"
int n=MaxV;int G[MaxV][MaxV];	//n为顶点数，MaxV为最大顶点数  G为邻接矩阵
int vis[MaxV] = {0};	//标记数组，vis[i]==true表示已访问。初始值均为false
Edge edge_prim[num]; //边集数组
int edge_num;//边数

int main()
{
	int choice=99;
	while(choice!=0)//按0退出
	{
	std::cout<<"-----电网建设造价设计-----"<<endl;
	Solution A;//创建一个对象A
	std::cout<<"请选择你要使用的算法(选择数字)"<<endl;
	std::cout<<"1. prim 算法"<<endl;
	std::cout<<"2. krusKal算法"<<endl;
	std::cout<<"3. KrusKal算法测试"<<endl;
	std::cout<<"4. prim算法测试"<<endl;
	std::cout<<"5. 按0退出"<<endl;
	cin>>choice;
	switch (choice)
	{
	case 1:
		std::cout<<"请输入小区个数(顶点数)"<<endl;cin>>n;A.vex=n;
		std::cout<<"请输入小区之间的路径数(边数)"<<endl;cin>>edge_num;
		//初始化邻接矩阵和边集数组
		A.initial_adj_matrix(edge_prim,n,edge_num);
		//创建邻接矩阵和边集数组
		A.create_adj_matrix(edge_prim,edge_num,n);
		A.adj_prim(vis,n,A.adj_matrix,edge_prim);
		break;
	case 2:
		std::cout<<"请输入小区个数(顶点数)"<<endl;cin>>n;A.vex=n;
		std::cout<<"请输入小区之间的路径数(边数)"<<endl;cin>>edge_num;
		//初始化邻接矩阵和边集数组
		A.initial_adj_matrix(edge_prim,n,edge_num);
		//创建边集数组
		A.create_adj_pn(A.adj_matrix,edge_num,n);
		A.adj_KrusKal(A.adj_pn,A.adj_matrix,edge_num);	
		break;
	case 3://测试KrusKal算法
		A.G(A.adj_matrix,edge_prim);//测试数据函数
		A.adj_KrusKal(edge_prim,A.adj_matrix,10);//调用Kruskal算法函数
		break;
	case 4://测试prim算法
		A.G(A.adj_matrix,edge_prim);//测试数据函数
		A.adj_prim(vis,n,A.adj_matrix,edge_prim);//调用Prim算法函数
		break;
	default:
		break;
	}
	}	
}
