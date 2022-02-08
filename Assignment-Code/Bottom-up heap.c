#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int H[100] = {0};
int n;
void downHeap(int i);
void printHeap();
void buildHeap();
void main() {
	int i;
	scanf("%d", &n);
	for (i = 1;i <= n;i++)
		scanf("%d", &H[i]);
	buildHeap();
	printHeap();
}
void buildHeap() {
	int i;
	for (i = n / 2;i >= 1;i--)
		downHeap(i);
}
void downHeap(int i) {
	int lc = 2 * i, rc = lc + 1, c, tmp;
	if (lc > n)
		return;
	if (lc==n || H[lc] >= H[rc])
		c = lc;
	else
		c = rc;
	if (H[i] < H[c]) {
		tmp = H[i];
		H[i] = H[c];
		H[c] = tmp;
		downHeap(c);
	}
	else 
		return;

}
void printHeap() {
	int i;
	for(i=1;i<=n;i++)
		printf(" %d", H[i]);
	printf("\n");
}
