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
}
int hash(int h,int M) {
	int val;
	val = h % M;
	return val;
}
void insertitem(NODE *T,int v) {
	NODE *p;getNode(&p);
	p->value = v;
	if (T->next == NULL) {
		T->next = p;
	}
	else {
		p->next = T->next;
		T->next = p;
	}
}
void searchitem(NODE *T, int v,int h) {
	NODE *p = T->next;
	int flag = 0, k = 0;
	if (p == NULL)
		printf("0\n");
	else {
		while (p!= NULL) {
			k++;
			if (p->value == v) {
				printf("%d\n", k);
				flag = 1;
				break;
			}
			p = p->next;
		}
		if (flag == 0)
			printf("0\n");
	}
}
void deletitem(NODE *T, int v,int h) {
	NODE *p = T, *q;
	int flag = 0, k = 0;
	if (p->next == NULL)
		printf("0\n");
	else {
		while (p->next != NULL) {
			k++;
			if (p->next->value == v) {
				if (p->next->next == NULL) {
					p->next = NULL;
				}
				else {
					p->next = p->next->next;
				}
				printf("%d\n", k);
				flag = 1;
				break;
			}
			p = p->next;
		}
		if (flag == 0)
			printf("0\n");
	}
}
void printitem(NODE **T,int M) {
	int i;
	NODE *p;
	for (i = 0;i < M;i++) {
		p = T[i]->next;
		while (p!=NULL) {
			printf(" %d", p->value);
			p = p->next;
		}
	}
}
int main() {
	int M, i, v, val;
	char ch;
	NODE **T = NULL;
	scanf("%d", &M);getchar();
	T = (NODE **)malloc(sizeof(NODE *)*M);
	for (i = 0;i < M;i++) {
		getNode(&T[i]);
	}
	while (1) {
		scanf("%c", &ch);getchar();
		if (ch == 'i') {
			scanf("%d", &v);getchar();
			insertitem(T[hash(v, M)],v);
		}
		else if (ch == 's') {
			scanf("%d", &v);getchar();
			searchitem(T[hash(v, M)], v, hash(v, M));
		}
		else if (ch == 'd') {
			scanf("%d", &v);getchar();
			deletitem(T[hash(v, M)], v, hash(v, M));
		}
		else if (ch == 'p') {
			printitem(T,M);
			printf("\n");
		}
		else if (ch == 'e')
			break;
	}
	return 0;
}
