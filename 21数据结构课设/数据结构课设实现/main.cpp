#include"graph.cpp"
int n=MaxV;int G[MaxV][MaxV];	//nΪ��������MaxVΪ��󶥵���  GΪ�ڽӾ���
int vis[MaxV] = {0};	//������飬vis[i]==true��ʾ�ѷ��ʡ���ʼֵ��Ϊfalse
Edge edge_prim[num]; //�߼�����
int edge_num;//����

int main()
{
	int choice=99;
	while(choice!=0)//��0�˳�
	{
	std::cout<<"-----��������������-----"<<endl;
	Solution A;//����һ������A
	std::cout<<"��ѡ����Ҫʹ�õ��㷨(ѡ������)"<<endl;
	std::cout<<"1. prim �㷨"<<endl;
	std::cout<<"2. krusKal�㷨"<<endl;
	std::cout<<"3. KrusKal�㷨����"<<endl;
	std::cout<<"4. prim�㷨����"<<endl;
	std::cout<<"5. ��0�˳�"<<endl;
	cin>>choice;
	switch (choice)
	{
	case 1:
		std::cout<<"������С������(������)"<<endl;cin>>n;A.vex=n;
		std::cout<<"������С��֮���·����(����)"<<endl;cin>>edge_num;
		//��ʼ���ڽӾ���ͱ߼�����
		A.initial_adj_matrix(edge_prim,n,edge_num);
		//�����ڽӾ���ͱ߼�����
		A.create_adj_matrix(edge_prim,edge_num,n);
		A.adj_prim(vis,n,A.adj_matrix,edge_prim);
		break;
	case 2:
		std::cout<<"������С������(������)"<<endl;cin>>n;A.vex=n;
		std::cout<<"������С��֮���·����(����)"<<endl;cin>>edge_num;
		//��ʼ���ڽӾ���ͱ߼�����
		A.initial_adj_matrix(edge_prim,n,edge_num);
		//�����߼�����
		A.create_adj_pn(A.adj_matrix,edge_num,n);
		A.adj_KrusKal(A.adj_pn,A.adj_matrix,edge_num);	
		break;
	case 3://����KrusKal�㷨
		A.G(A.adj_matrix,edge_prim);//�������ݺ���
		A.adj_KrusKal(edge_prim,A.adj_matrix,10);//����Kruskal�㷨����
		break;
	case 4://����prim�㷨
		A.G(A.adj_matrix,edge_prim);//�������ݺ���
		A.adj_prim(vis,n,A.adj_matrix,edge_prim);//����Prim�㷨����
		break;
	default:
		break;
	}
	}	
}
