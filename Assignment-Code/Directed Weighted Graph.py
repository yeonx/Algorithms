#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
int N, M, S;
typedef struct vertex {
	int num;
	int flag;
	int print;
	int pre;
}v;
typedef struct edge {
	int a, b;
	int weight;
	int pass;
	struct edge *enext;
}e;
v **V;
e *H_edge;
void getvnode(v **p) {
	(*p) = (v *)malloc(sizeof(v));
	(*p)->flag = 0;
	(*p)->print = 1000;
}
void getenode(e **p) {
	(*p) = (e *)malloc(sizeof(e));
	(*p)->enext = NULL;
	(*p)->pass = 0;
}
void addenode(int a, int b, int w) {
	e *q, *p;
	getenode(&q);
	q->a = a;
	q->b = b;
	q->weight = w;
	for (p = H_edge;p->enext != NULL;p = p->enext);
	p->enext = q;
}
int *A;
void vo(int a) {
	int i, k = 0;
	for (i = 0;i < N;i++) {
		if (A[i] == a) {
			V[i]->flag = 0;
			k = 1;
			vo(i + 1);
		}
	}
	if (k == 0)
		return;
}
void graph() {
	int i = S, j, min, flag;V[i - 1]->flag = 1;
	V[i - 1]->print = 0;
	e *p;
	int kkk = 0;
	while (1) {
		V[i - 1]->flag = 1;
		for (p = H_edge->enext;p != NULL;p = p->enext) {
			if (p->a == i) {
				j = p->b;
				if (j == S)
					continue;
				if (p->weight < 0)
					kkk = 1;
				if ((V[j - 1]->flag == 1) && (kkk == 1)) {
					if ((V[j - 1]->print) > ((V[i - 1]->print) + (p->weight))) {
						V[j - 1]->print = V[i - 1]->print + p->weight;
						V[j - 1]->flag = 0;
						vo(j);
						continue;
					}
				}
				if (V[j - 1]->flag == 1)
					continue;
				if (V[j - 1]->print == 100) {
					V[j - 1]->print = p->weight + (V[i - 1]->print);
					V[j - 1]->pre = i;
					A[j - 1] = i;
				}
				else if ((V[j - 1]->print) > (V[i - 1]->print + p->weight)) {
					V[j - 1]->print = V[i - 1]->print + p->weight;
					V[j - 1]->pre = i;
					A[j - 1] = i;
				}
			}
		}

		min = 1000;
		flag = 0;
		for (int j = 0;j < N;j++) {
			if (j == S - 1)
				continue;
			if (V[j]->print == 1000) {
				continue;
			}
			if (V[j]->flag == 1)
				continue;
			if (min > V[j]->print) {
				min = V[j]->print;
				i = j + 1;
				flag = 1;

			}

		}
		
		if (flag == 0)
			break;

	}
}

void main() {
	int i;
	int n, m, l;
	v *p;
	scanf("%d %d %d", &N, &M, &S);
	V = (v **)malloc(sizeof(v *)*N);
	A = (int*)malloc(sizeof(int)*N);
	getenode(&H_edge);
	for (i = 0;i < N;i++) {
		getvnode(&V[i]);
		V[i]->num = i + 1;
		A[i] = 1000;
	}
	A[S - 1] = 0;
	for (i = 0;i < M;i++) {
		scanf("%d %d %d", &n, &m, &l);
		addenode(n, m, l);
	}
	graph();
	for (i = 0;i < N;i++) {
		if (i == S - 1)
			continue;
		if (V[i]->print == 1000)
			continue;
		printf("%d %d\n", V[i]->num, V[i]->print);
	}
}
/*

5 7 1
1 2 1
1 4 5
5 1 -2
3 5 3
3 4 1
1 3 2
3 2 -3

*/
