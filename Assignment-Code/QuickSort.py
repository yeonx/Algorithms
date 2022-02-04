#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int find(int *L, int ll, int rr) {
	int mid, pivot, l, r;
	if (rr - ll <= 1) {
		return ll;
	}
	srand((unsigned int)time(NULL));
	l= (int)(rand() % (rr - ll + 1) + ll);
	mid = (int)(rand() % (rr - ll + 1) + ll);
	r= (int)(rand() % (rr - ll + 1) + ll);
	if ((L[l] <= L[mid] && L[mid] <= L[r])||(L[l] >= L[mid] && L[mid] >= L[r]))
		return mid;
	else if ((L[l] <= L[r] && L[r] <= L[mid])||(L[l] >= L[r] && L[r] >= L[mid]))
		return r;
	else
		return l;
}
int partition(int *L, int l, int r, int k) {
	int tmp, pivot = L[k];
	int i = l, j = r - 1, o;
	tmp = L[k];L[k] = L[r];L[r] = tmp;
	while (i <= j) {
		while (i <= j && L[i] < pivot) i++;
		while (i <= j && L[j] >= pivot) j--;
		if (i < j) {
			tmp = L[i]; L[i] = L[j]; L[j] = tmp;
		}
	}
	tmp = L[i];L[i] = L[r];L[r] = tmp;

	return i;
}
void quicksort(int *L, int l, int r) {
	int k, b, i;
	if (l >= r)
		return;
	k = find(L, l, r);
	b = partition(L, l, r, k);
	quicksort(L, l, b - 1);
	quicksort(L, b + 1, r);
}
void main() {
	int N, *L = NULL, i;
	scanf("%d", &N);
	L = (int *)malloc(sizeof(int)*N);
	for (i = 0;i < N;i++)
		scanf("%d", &L[i]);
	quicksort(L, 0, N - 1);
	for (i = 0;i < N;i++)
		printf(" %d", L[i]);
	free(L);
}
