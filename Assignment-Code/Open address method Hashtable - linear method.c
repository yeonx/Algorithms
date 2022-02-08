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
void insertitem(NODE **T,int v,int M) {
	NODE *p;getNode(&p); p->value = v;
	int i, h = hash(v, M);
	if (T[h]->next == NULL) {
		T[h]->next=p;
		printf("%d\n", h);
	}
	else {
		while (1) {
			printf("C");
			h++;
			if (h == M)
				h = 0;
			if (T[h]->next == NULL) {
				T[h]->next = p;
				printf("%d\n", h);
				break;
			}
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
int main() {
	int N, M, i, v, val;
	char ch;
	NODE **T = NULL;
	scanf("%d %d", &M,&N);getchar();
	T = (NODE **)malloc(sizeof(NODE *)*M);
	for (i = 0;i < M;i++) {
		getNode(&T[i]);
	}
	while (1) {
		scanf("%c", &ch);getchar();
		if (ch == 'i') {
			scanf("%d", &v);getchar();
			insertitem(T,v,M);
		}
		else if (ch == 's') {
			scanf("%d", &v);getchar();
			searchitem(T,v,M);
		}
		else if (ch == 'e')
			break;
	}
	return 0;
}
