#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void insertion(int arr[], int n);
int main() {
	int n, *arr = NULL;
	int i;
	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int)*n);
	for (i = 0;i < n;i++)
		scanf("%d", &arr[i]);
	insertion(arr, n);
	for (i = 0;i < n;i++)
		printf(" %d", arr[i]);
	free(arr);
	return 0;
}
void insertion(int arr[], int n) {
	int  i, j, tmp;
	for (i = 1;i < n;i++) {
		tmp = arr[i];
		for (j = i - 1;j >= 0;j--) {
			if (tmp > arr[j])
				break;
			arr[j + 1] = arr[j];
		}
		arr[j + 1] = tmp;
	}
}
