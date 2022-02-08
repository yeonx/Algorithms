#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int H[100] = {0};
int n=0;
void insertItem(int key);
void upHeap(int i);
int removeMax();
void printHeap();
void main() {
	char ch; int key;
	while (1) {
		scanf("%c", &ch); getchar();
		if (ch == 'i') {
			scanf("%d", &key); getchar();
			insertItem(key);
		}
		else if (ch == 'd')
			printf("%d\n",removeMax());
		else if (ch == 'p')
			printHeap();
		else
			break;
	}
}
void upHeap(int i) {
	int tmp;
	if (i > 1 && H[i / 2] < H[i]) {
		tmp = H[i / 2]; H[i / 2] = H[i]; H[i] = tmp;
		upHeap(i / 2);
	}
	else
		return;
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
void insertItem(int key) {
	n++;
	H[n] = key;
	upHeap(n);
	printf("0\n");
}
int removeMax() {
	int root = H[1];
	H[1] = H[n]; n--;
	downHeap(1);
	return root;
}
void printHeap() {
	int i;
	for(i=1;i<=n;i++)
		printf(" %d", H[i]);
	printf("\n");
}
