#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
typedef struct enode {
	int s, e;
	int enumber;
	struct enode *next;
}edge;
typedef struct vnode {
	edge *enext;
}vertex;
void getedge(edge **p) {
	(*p) = (edge *)malloc(sizeof(edge));
	(*p)->next = NULL;
}
void getv(vertex **p) {
	(*p) = (vertex *)malloc(sizeof(vertex));
	getedge(&((*p)->enext));
}
void addedge(vertex *v,int i,int j,int k) {
	edge *p =v->enext;
	edge *q; getedge(&q);
	q->s = i;q->e = j;q->enumber = k;
	if (p == NULL)
		p = q;
	else {
		while (p->next != NULL) {
			if (p->next->e > q->e)
				break;
			p = p->next;
		}
		if (p->next != NULL)
			q->next = p->next;
		p->next = q;
	}
}
void printnode(int n,vertex *v) {
	edge *p = v->enext->next;
	if (p == NULL) {
		printf("-1\n");
		return;
	}
	else {
		while (p != NULL) {
			printf(" %d %d", p->e, p->enumber);
			p = p->next;
		}
		printf("\n");
	}
}
void changenode(int a, int b, int n,vertex *v) {
	edge *p, *q;
	int j = 0;
	for (p = v->enext;p->next!=NULL;p = p->next) {
		if (p->next->e == b) {
			j = 1;
			if (n != 0) {
				p->next->enumber = n;
			}
			else {
				q = p->next;
				if (p->next->next == NULL)
					p->next = NULL;
				else {
					p->next = p->next->next;
				}
				free(q);
			}
			break;
		}
	}
	if (j == 0 && n!=0) {
		addedge(v, a, b, n);
	}
}
int main() {
	vertex **v;
	v = (vertex **)malloc(sizeof(vertex*)*6);
	int i;
	for (i = 0;i < 6;i++) {
		getv(&v[i]);
	}
	addedge(v[0], 1, 2, 1);
	addedge(v[0], 1, 3, 1);
	addedge(v[0], 1, 4, 1);
	addedge(v[0], 1, 6, 2);
	addedge(v[1], 2, 1, 1);
	addedge(v[1], 2, 3, 1);
	addedge(v[2], 3, 1, 1);
	addedge(v[2], 3, 2, 1);
	addedge(v[2], 3, 5, 4);
	addedge(v[3], 4, 1, 1);
	addedge(v[4], 5, 3, 4);
	addedge(v[4], 5, 5, 4);
	addedge(v[4], 5, 6, 3);
	addedge(v[5], 6, 1, 2);
	addedge(v[5], 6, 5, 3);
	char c;
	int a, b, n;
	while (1) {
		scanf("%c", &c);getchar();
		if (c == 'q')
			break;
		else if (c == 'a') {
			scanf("%d", &n);getchar();
			if (n < 1 || n>6) 
				printf("-1\n");
			else
				printnode(n,v[n-1]);
		}
		else if (c == 'm') {
			scanf("%d %d %d", &a, &b, &n);getchar();
			if (a < 1 || a>6 || b < 1 || b>6)
				printf("-1\n");
			else {
				changenode(a, b, n, v[a - 1]);
				changenode(b, a, n, v[b - 1]);
			}
		}
	}
	return 0;
}
