#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
int findkey(int *a,int key,int start,int end) {
	int i = (start + end) / 2;
	if (a[0] > key)
		return -1;
	if (a[i] == key)
		return i;
	else if (a[i] > key) {
		if (end - start == 1)
			return i;
		findkey(a, key, start, i);
	}
	else {
		if (end - start == 1)
			return i;
		findkey(a, key, i, end);
	}
}
int main() {
	int N, k, *a = NULL;
	scanf("%d %d", &N, &k);
	a = (int *)malloc(sizeof(int)*N);
	for (int i=0;i < N;i++)
		scanf("%d", &a[i]);
	printf(" %d", findkey(a, k, 0, N));
	free(a);
	return 0;
}
