#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
typedef struct node {
	struct node *next;
	int data;
}NODE;
typedef struct{
	NODE *L1;
	NODE *L2;
}TWO;
void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
	(*p)->next = NULL;
}
void addNode(NODE *H) {
	NODE *tmp, *p;
	getNode(&tmp);
	int n;
	scanf("%d", &n);
	tmp->data = n;
	for (p = H;p->next != NULL;p = p->next);
	p->next = tmp;
}
void mergeSort(NODE **L,int N);
NODE *merge(NODE **L1, NODE **L2);
TWO partition(NODE *L, int k);
int main() {
	NODE *L, *p;
	getNode(&L);
	int N;
	scanf("%d", &N);
	for (int i = 0;i < N;i++)
		addNode(L);
	mergeSort(&L->next,N);
	for (p = L->next;p != NULL;p = p->next)
		printf(" %d", p->data);
	return 0;
}
void mergeSort(NODE **L,int N) {
	TWO list;
	NODE *A, *B, *p = *L;
	if (N > 1) {
		list = partition(p, N / 2);
		A = list.L1; B = list.L2;
		mergeSort(&A, N / 2);
		mergeSort(&B, (N + 1) / 2);
		*L = merge(&A, &B);
	}
}
NODE *merge(NODE **L1, NODE **L2) {
	NODE *L = NULL, *I = NULL;
	NODE *A = *L1, *B = *L2;
	if (A->data <= B->data) {
		L = A;
		A = A->next;
	}
	else {
		L = B;
		B = B->next;
	}
	I = L;
	while (1) {
		if (A == NULL && B == NULL)
			break;
		if (B == NULL && A != NULL) {
			I->next = A;
			A = A->next;
			I = I->next;
		}
		else if (A == NULL && B != NULL) {
			I->next = B;
			B = B->next;
			I = I->next;
		}
		else if (A->data <= B->data) {
			I->next = A;
			A = A->next;
			I = I->next;
		}
		else if (A->data >= B->data) {
			I->next = B;
			B = B->next;
			I = I->next;
		}
	}
	return L;
}
TWO partition(NODE *L, int k) {
	TWO list;
	NODE *A, *B, *p=L;
	A = L;
	for (int i = 0;i < k-1;i++)
		p = p->next;
	B = p->next;
	p->next = NULL;
	list.L1 = A; list.L2 = B;
	return list;
}
