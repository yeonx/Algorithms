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
void DFS(VNODE *S) {
	int i;
	ENODE *p;
	if (S->vi == 0) {
		printf("%d\n", S->num);
		S->vi = 1;
	}
	for (p = S->edge->next;p!=NULL;p=p->next) {
		if (p->c->vi == 0)
			DFS(p->c);
	}
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
	DFS(v[S - 1]);
	return 0;
}
