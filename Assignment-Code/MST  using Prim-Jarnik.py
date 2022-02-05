#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
int N, M;
int **graph = NULL, *answer = NULL, *q = NULL;
int MIN = 0;
void prim() {
	int i = 0, j, min = 1000, min_index, flag;
	answer[0] = 1; q[0] = -1;
	int a = 1;
	printf(" 1");
	while(1) {
		for (j = 0;j < N;j++) {
			if (i == j || graph[i][j] == 0)
				continue;
			if (q[j]==0||q[j] > graph[i][j]) {
				q[j] = graph[i][j];
			}
			graph[j][i] = 0;
		}
		min_index = 0;min = 1000;
		for (j = 1;j < N;j++) {
			if (q[j] == -1||q[j]==0)
				continue;
			if (min > q[j]) {
				min_index = j;
				min = q[j];
			}
		}
		q[min_index] = -1;
		i = min_index;
		MIN += min;
		answer[a] = min_index + 1;
		printf(" %d", answer[a]);
		a++;
		
		if (a == N)
			break;
	}
}
void main() {
	int i, a, b, j;
	scanf("%d %d", &N, &M);
	graph = (int **)malloc(sizeof(int *)*N);
	answer = (int *)malloc(sizeof(int)*N);
	q= (int *)malloc(sizeof(int)*N);
	for (i = 0;i < N;i++){
		q[i] = 0;
		graph[i] = (int *)malloc(sizeof(int)*N);
		for (j = 0;j < N;j++)
			graph[i][j] = 0;
	}
	for (i = 0;i < M;i++) {
		scanf("%d %d", &a, &b);
		scanf("%d", &graph[a-1][b-1]);
		graph[b-1][a-1] = graph[a-1][b-1];
	}
	prim();
	printf("\n%d", MIN);
}
