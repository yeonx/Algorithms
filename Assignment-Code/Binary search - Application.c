#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int findkey(char *str,int n, int start, int end) {
	int i = (start + end) / 2;
	if (start == end)
		return i;
	if (str[n] == 'N') 
		findkey(str, n+1, start, i);
	else if (str[n] == 'Y') 
		findkey(str, n+1, i+1, end);
}
int main() {
	int a, b, n;
	char *str = NULL;
	scanf("%d %d %d", &a, &b,&n);
	str = (char *)malloc(sizeof(char)*(n + 1));
	scanf("%s", str);
	printf(" %d", findkey(str,0,a,b));
	free(str);
	return 0;
}
