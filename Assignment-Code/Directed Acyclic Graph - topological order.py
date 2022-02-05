#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
typedef struct enode ENODE;
typedef struct vnode VNODE;
typedef struct enode {
	struct enode *next;
	VNODE *v;
}ENODE;
typedef struct vnode {
	int I;
	char name;
	ENODE *outedge;
	ENODE *inedge;
	int inDegree;
}VNODE;
typedef struct queue {
	struct queue *next;
	VNODE *vertex;
}Queue;
void getq(Queue **p) {
	(*p) = (Queue *)malloc(sizeof(Queue));
	(*p)->next = NULL;
	(*p)->vertex = NULL;
}
void getenode(ENODE **p) {
	(*p) = (ENODE *)malloc(sizeof(ENODE));
	(*p)->next = NULL;
	(*p)->v = NULL;
}

VNODE **G;
Queue *Q;
int n, m;
int *top;

void buildGraph(); 
//표준 입력으로부터 방향그래프 정보를 읽어 들여 그래프 G에 저장
void insertVertex(char vName, int i); 
// vName 정점 i에 G의 정점리스트에 삽입하고 i의 진입자수를 초기화
void insertDirectedEdge(char uName, char wName, int i);
//uName 정점 u를 시점으로, wName 정점 w를 종점으로 하는 방향간선 i를, G의 간선리스트,
//u의 진출간선리스트, 그리고 w의 진입간선리스트에 각각 삽입하고 w의 진입차수를 갱신
int index(char vName);
//vName에 해당하는 정점의 인덱스를 찾아 반환
void enqueue(VNODE *g);
int dequeue();
void topologicalSort();
void main() {
	int i;
	buildGraph();
	topologicalSort();
	if (top[0] == 0)
		printf("%d\n", 0);
	else {
		for (i = 1;i <= n;i++) {
			printf("%c ", G[top[i]]->name);
		}
	}
}
void buildGraph() {
	int i;
	char vName, uName, wName;
	
	scanf("%d", &n);

	G = (VNODE **)malloc(sizeof(VNODE)*n);
	top = (int *)malloc(sizeof(int)*(n+1));

	for (i = 0;i < n;i++) {
		getchar();
		scanf("%c", &vName);
		insertVertex(vName, i);
	}
	scanf("%d", &m);
	for (i = 0;i < m;i++) {
		getchar();scanf("%c", &uName);getchar();scanf("%c", &wName);
		insertDirectedEdge(uName, wName, i);
	}
}
void insertVertex(char vName, int i) {
	G[i] = (VNODE*)malloc(sizeof(VNODE));
	G[i]->name = vName;
	G[i]->outedge = (ENODE *)malloc(sizeof(ENODE));
	G[i]->inedge = (ENODE *)malloc(sizeof(ENODE));
	G[i]->inedge->next = NULL;
	G[i]->outedge->next = NULL;
	G[i]->inDegree = 0;
	G[i]->I = i;
}
void insertDirectedEdge(char uName, char wName, int i) {
	int u = index(uName);
	int w = index(wName);
	ENODE *p;getenode(&p);p->v = G[u];
	ENODE *q;getenode(&q);q->v = G[w];
	if (G[w]->inedge->next == NULL) {
		G[w]->inedge->next = p;
	}
	else {
		p->next = G[w]->inedge->next;
		G[w]->inedge->next = p;
	}
	if (G[u]->outedge->next == NULL) {
		G[u]->outedge->next = q;
	}
	else {
		q->next = G[u]->outedge->next;
		G[u]->outedge->next = q;
	}
	G[w]->inDegree++;

}
int index(char vName) {
	int i;
	for (i = 0;i < n;i++) {
		if (G[i]->name == vName)
			return i;
	}
}

void topologicalSort() {
	ENODE *p;
	int u, w;
	getq(&Q);
	int *in, t = 1;
	in = (int *)malloc(sizeof(int)*n);
	int i;
	for (i = 0;i < n;i++) {
		in[i] = G[i]->inDegree;
		if (in[i] == 0) {
			enqueue(G[i]);
		}
	}
	while (Q->next != NULL) {
		u = dequeue();
		top[t] = u;
		t++;
		for (p = G[u]->outedge->next;p != NULL;p = p->next) {
			w = p->v->I;
			in[w]--;
			if (in[w] == 0)
				enqueue(G[w]);
		}
	}
	if (t < n)
		top[0] = 0;
	else
		top[0] = 1;
}
void enqueue(VNODE *g) {
	Queue *p;getq(&p);
	Queue *i;
	for (i = Q;;i = i->next) {
		if (i->next == NULL) {
			i->next = p;
			break;
		}
	}
	p->vertex = g;
}
int dequeue() {
	Queue *p = Q->next;
	int u = p->vertex->I;

	if (p->next == NULL)
		Q->next = NULL;
	else
		Q->next = p->next;

	return u;
}
