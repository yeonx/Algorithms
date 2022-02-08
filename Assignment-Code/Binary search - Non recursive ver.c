#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
void findkey(int *a, int N, int k) {
	int mid = N / 2, i, start = 0, end = N - 1, tmp;
	while (end>start) {
		if (k > a[N - 1]) {
			printf(" %d", N);
			break;
		}
		else if (k < a[0]) {
			printf(" 0");
			break;
		}
		if (a[mid] == k) {
			printf(" %d", mid);
			break;
		}
		else if (a[mid] > k) {
			end = mid; 
			mid = (start+end) / 2;
		}
		else if(a[mid]<k){
			start = mid;
			mid = (start + end) / 2;
		}
		if(mid==start){
			printf(" %d", mid+1);
			break;
		}
		else if (mid == end) {
			printf(" %d", mid);
			break;
		}
	}
}
int main() {
	int N, k, *a = NULL;
	scanf("%d %d", &N, &k);
	a = (int *)malloc(sizeof(int)*N);
	for (int i = 0;i < N;i++)
		scanf("%d", &a[i]);
	findkey(a, N, k);
	free(a);
	return 0;
}
