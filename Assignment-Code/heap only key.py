#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
int H[100] = { 0 }, n;
int m = 0, N;
void insertItem(int key);
void upHeap(int i);
void downHeap(int i);
void inPlaceHeapSort();
void printArray();
void main() {
	int key, i;
	scanf("%d", &n);
	N = n;
	for (i = 0;i < n;i++) {
		scanf("%d", &key);
		m++;
		insertItem(key);
	}
	inPlaceHeapSort();
	printArray();
}
void insertItem(int key) {
	H[m] = key;
	upHeap(m);
}
void upHeap(int i) {
	int p, tmp;
	for (p = i / 2;i != 1;p = i / 2) {
		if (H[i] > H[p]) {
			tmp = H[i];
			H[i] = H[p];
			H[p] = tmp;
			i = p;
		}
		else
			break;
	}
}
void downHeap(int i) {
	int tmp;
	int p, c, lc, rc;
	for (p = i;;p=c) {
		lc = p * 2;
		rc = p * 2 + 1;
		if (lc > N)
			break;
		else if (rc > N)
			c = lc;
		else {
			if (H[lc] >= H[rc])
				c = lc;
			else
				c = rc;
		}
		if (H[p] < H[c]) {
			tmp = H[p];
			H[p] = H[c];
			H[c] = tmp;
		}
		else
			break;
	}
}
void inPlaceHeapSort() {
	int i, tmp;
	for (i = n;i>1;i--) {
		tmp = H[1];
		H[1] = H[i];
		H[i] = tmp;
		N--;
		downHeap(1);
	}
}
void printArray(){
	int i;
	for (i = 1;i <= n;i++) {
		printf(" %d", H[i]);
	}
	printf("\n");
}
