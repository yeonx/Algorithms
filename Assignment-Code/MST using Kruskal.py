#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
int N, M;
int **graph = NULL, *answer = NULL, *q = NULL;
int MIN = 0;
void kruskal() {
	int i, j, min = 1000, min_index, flag, a = 0, b = 0, v = 0, f;
	while (1) {
		min = 1000;
		if (v == N - 1)
			break;
		for (i = 0;i < N;i++) {
			for (j = 0;j < N;j++) {
				if ((q[i]==q[j]) && (q[i]!=0)) {
					continue;
				}
				if (graph[i][j] != 0 && graph[i][j] < min) {
					min = graph[i][j];
					a = i;b = j;
				}
			}
		}
		
		graph[a][b] = 0;
		graph[b][a] = 0;
		answer[v] = min;v++;
		MIN += min;
		if (v==1) {
			q[a] = 1;q[b] = 1;
		}
		else if ((q[a]==0&&q[b]!=0)||(q[a] != 0 && q[b] == 0)) {
			if (q[a] == 0)
				q[a] = q[b];
			else
				q[b] = q[a];
		}
		else if (q[a] != q[b]) {
			if (q[a] < q[b]) {
				flag = q[b];
				q[b] = q[a];
				f = q[a];
			}
			else {
				flag = q[a];
				q[a] = q[b];
				f = q[a];
			}
			for (i = 0;i < N;i++) {
				if (q[i] == flag) {
					q[i] = f;
				}
			}
		}
		else {
			q[a] = v;q[b] = v;
		}
	}
}
void main() {
	int i, a, b, j;
	scanf("%d %d", &N, &M);
	graph = (int **)malloc(sizeof(int *)*N);
	answer = (int *)malloc(sizeof(int)*(N-1));
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
	kruskal();
	for (i = 0;i < N - 1;i++) {
		printf("%d ", answer[i]);
	}
	printf("\n%d", MIN);
}
