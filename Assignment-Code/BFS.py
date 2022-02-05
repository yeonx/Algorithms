#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
typedef struct enode ENODE;
typedef struct vnode VNODE;
typedef struct enode {
	struct enode *next;
	VNODE *c;
}ENODE;
typedef struct vnode {
	ENODE *edge;
	int vi;
	int num;
}VNODE;
void getenode(ENODE **p) {
	(*p) = (ENODE *)malloc(sizeof(ENODE));
	(*p)->next = NULL;
}
void getvnode(VNODE **p,int k) {
	(*p) = (VNODE *)malloc(sizeof(VNODE));
	(*p)->num = k;
	(*p)->vi = 0;
	getenode(&((*p)->edge));
}
void addedge(VNODE *a, VNODE *b) {
	ENODE *p;
	ENODE *q;getenode(&q);
	int flag = 0;
	q->c = b;
	if (a->edge->next == NULL) {
		a->edge->next = q;
	}
	else {
		p = a->edge;
		while (p->next!=NULL) {
			if ((p->next->c->num) > (b->num)) {
				q->next = p->next;
				p->next = q;
				flag = 1;
				break;
			}
			p = p->next;
		}
		if (flag == 0) {
			p->next = q;
		}
	}
}
void BFS(VNODE **v,int S, int N) {
	int *Q, i,front=0, rear=0;
	Q = (int *)malloc(sizeof(int)*N);
	for (i = 0;i < N;i++)
		Q[i] = 0;
	ENODE *p = v[S - 1]->edge->next;
	Q[0] = v[S-1]->num; v[S-1]->vi = 1;
	while (rear!=N-1) {
		for (;p != NULL;p = p->next) {
			if (p->c->vi == 0) {
				rear++;
				Q[rear] = p->c->num; p->c->vi = 1;
			}
		}
		front++;
		p = v[Q[front] - 1]->edge->next;
	}
	for (i = 0;i < N;i++)
		printf("%d\n", Q[i]);
}
 int main() {
	VNODE **v;
	int N, M, S, i, a, b, j;
	scanf("%d %d %d",&N, &M, &S);
	v = (VNODE **)malloc(sizeof(VNODE)*N);
	for (i = 0;i < N;i++) {
		getvnode(&v[i],i+1);
	}
	for (i = 0;i < M;i++) {
		scanf("%d %d", &a, &b);
		addedge(v[a - 1], v[b - 1]);
		addedge(v[b - 1], v[a - 1]);
	}
	BFS(v,S,N);
	return 0;
}
