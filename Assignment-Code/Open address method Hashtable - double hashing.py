#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
typedef struct node {
	int value;
	struct node *next;
}NODE;
void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
	(*p)->next = NULL;
	(*p)->value = 0;
}
int hash(int h,int M) {
	int val;
	val = h % M;
	return val;
}
int hash2(int h, int q) {
	int val;
	val = q - (h % q);
	return val;
}
int doublehashing(int h,int i,int M,int q) {
	int val;
	val = (hash(h,M) + i * hash2(h,q)) % M;
	return val;
}
void insertitem(NODE **T,int v,int M,int q) {
	NODE *p;getNode(&p); p->value = v;
	int i = 0, h, j;
	for (i = 0;i<M;i++) {
		h = doublehashing(v, i, M, q);
		if (T[h]->next == NULL) {
			T[h]->next = p;
			for (j = 0;j < i;j++)
				printf("C");
			printf("%d\n", h);
			break;
		}

	}
}
void searchitem(NODE **T, int v,int M) {
	int i, flag = 0;
	NODE *p;
	for (i = 0;i < M;i++) {
		p = T[i]->next;
		if (p != NULL && p->value==v) {
			printf("%d %d\n", i,v);
			flag = 1;
			break;
		}
	}
	if (flag == 0)
		printf("-1\n");
}
void printitem(NODE **T, int M) {
	NODE *p;
	int i;
	for (i = 0;i < M;i++) {
		p = T[i]->next;
		if (p == NULL)
			printf(" 0");
		else
			printf(" %d",p->value);
	}
	printf("\n");
}
int main() {
	int N, M, i, v, q;
	char ch;
	NODE **T = NULL;
	scanf("%d %d %d", &M,&N,&q);getchar();
	T = (NODE **)malloc(sizeof(NODE *)*M);
	for (i = 0;i < M;i++) {
		getNode(&T[i]);
	}
	while (1) {
		scanf("%c", &ch);getchar();
		if (ch == 'i') {
			scanf("%d", &v);getchar();
			insertitem(T,v,M,q);
		}
		else if (ch == 's') {
			scanf("%d", &v);getchar();
			searchitem(T,v,M);
		}
		else if (ch == 'p') {
			printitem(T,M);
		}
		else if (ch == 'e') {
			printitem(T, M);
			break;
		}
	}
	return 0;
}
