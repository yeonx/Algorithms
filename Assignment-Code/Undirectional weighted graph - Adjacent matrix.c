#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
int arr[6][6] = { {0,1,1,1,0,2},{1,0,1,0,0,0},{1,1,0,0,4,0},{1,0,0,0,0,0},{0,0,4,0,4,3},{2,0,0,0,3,0} };
void findnode(int n) {
	int i, j = -1;
	if (n < 1 || n>6) {
		printf("-1\n");
		return;
	}
	for (i = 0;i < 6;i++) {
		if (arr[n - 1][i] != 0) {
			j = 0;
			printf(" %d %d", i+1, arr[n-1][i]);
		}
	}
	if (j == -1)
		printf("%d", j);
	printf("\n");
}
void chagenode(int a, int b, int n) {
	if ((a < 1 || a>6) || (b < 1 || b>6))
		printf("-1\n");
	else {
		arr[a - 1][b - 1] = n;
		arr[b - 1][a - 1] = n;
	}
}
int main() {
	int n;
	int a, b;
	char c;
	while (1) {
		scanf("%c", &c);getchar();
		if (c == 'q')
			break;
		else if (c == 'a') {
			scanf("%d", &n);getchar();
			findnode(n);
		}
		else if (c == 'm') {
			scanf("%d %d %d", &a, &b, &n);getchar();
			chagenode(a, b, n);
		}
	}
	return 0;
}
