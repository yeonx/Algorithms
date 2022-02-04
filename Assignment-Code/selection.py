#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//select sorting
void printall(int a[],int n) {
	int i;
	for (i = 0;i < n;i++)
		printf(" %d", a[i]);
	printf("\n");
}
int findbig(int *a, int n,int p) {
	int big = -1;
	int i;
	for (i = 0;i < n;i++) {
		if (big == -1 && p < a[i]) {
			big = i;
		}
		else if (big != -1 && a[big] < a[i])
			big = i;
	}
	return big;
}
void selectsort(int *a, int n) {
	int i, j, tmp;
	for (i = n - 1;i > 0;i--) {
		j=findbig(a, i,a[i]);
		if (j != -1) {
			tmp = a[i];
			a[i] = a[j];
			a[j] = tmp;
		}
	}
}
int main() {
	int *a = NULL, n, i, j;
	scanf("%d", &n);
	a = (int *)malloc(sizeof(int)*n);
	for (i = 0;i < n;i++) 
		scanf("%d", &a[i]);
	selectsort(a, n);
	printall(a, n);
	free(a);
	return 0;
}
