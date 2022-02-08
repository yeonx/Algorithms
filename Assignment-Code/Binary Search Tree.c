#pragma warning(disable:4996)
#include<stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct node {
	struct node *parent;
	struct node *lChild;
	struct node *rChild;
	int key;
}NODE;
void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
	(*p)->lChild = NULL;
	(*p)->parent = NULL;
	(*p)->rChild = NULL;
}
int isExternal(NODE *w);
int isInternal(NODE *w);
NODE *sibling(NODE *w);
NODE *inOrderSucc(NODE *w);
NODE *reduceExternal(NODE *r,NODE *z);
NODE *treeSearch(NODE *w, int k);
int findElement(NODE *w, int k);
void insertItem(NODE *w, int k);
int removeElement(NODE *w, int k);
void printnode(NODE *w);
void main() {
	char ch;
	int key, l;
	NODE *w; getNode(&w);
	while (1) {
		scanf("%c", &ch);
		if (ch == 'i') {
			scanf("%d", &key);
			insertItem(w, key);
			getchar();
		}
		else if (ch == 'd') {
			scanf("%d", &key);
			l = removeElement(w, key);
			if (l == -1) 
				printf("X\n");
			else 
				printf("%d\n", l);
			getchar();
		}
		else if (ch == 's') {
			scanf("%d", &key);
			l = findElement(w, key);
			if (l==-1)
				printf("X\n");
			else 
				printf("%d\n", l);
			getchar();
		}
		else if (ch == 'p') {
			printnode(w);
			printf("\n");
		}
		else if (ch == 'q')
			break;
	}
}
int isExternal(NODE *w) {
	if ((w->lChild == NULL) && (w->rChild == NULL))
		return 1;
	else
		return 0;
}
int isInternal(NODE *w) {
	if ((w->lChild != NULL) || (w->rChild != NULL))
		return 1;
	else
		return 0;
}
NODE *sibling(NODE *w) { //형제노드반환
	if (w->parent == NULL) //루트노드
		return;
	if (w->parent->lChild == w) //왼쪽이 자신이면
		return w->parent->rChild; //오른쪽이 형제
	else
		return w->parent->lChild; 
}
NODE *inOrderSucc(NODE *w) {
	w = w->rChild; //오른쪽자식
	if (isExternal(w)) //외부노드
		return;
	while (1) {
		if (isExternal(w->lChild))
			return w;
		w = w->lChild;
	}
	return w;
}
NODE *reduceExternal(NODE *r,NODE *z) { //외부노드인 z넣고 , 사라지는 z의 부모노드 반환
	NODE *w = z->parent;  //z의 부모노드
	NODE *zs = sibling(z); //z의 형제 노드
	NODE *g;
	if (w->parent == NULL) { // z의 부모노드가 루트
		*r=*zs;
	}
	else { //부모노드가 루트가 아님
		g = w->parent; //부모의 부모노드
		zs->parent = g; //형제의 부모노드를 부모의 부모노드로 대체
		if (w == g->lChild) // 부모노드가 왼쪽이면
			g->lChild = zs; //그 자리를 대체
		else
			g->rChild = zs;
	}
	return zs;
}
NODE *treeSearch(NODE *w, int k) {
	if (isExternal(w)) //외부노드라면
		return w; //그대로 반환
	if (w->key == k)
		return w;
	else if (k < w->key)
		return treeSearch(w->lChild, k);
	else
		return treeSearch(w->rChild, k);
}
int findElement(NODE *w, int k) {
	NODE *q = w;
	while (1) {
		if (q->key == k)
			return k;
		else if (k < q->key) {
			if (q->lChild == NULL)
				return -1;
			q = q->lChild;
		}
		else if (k > q->key) {
			if (q->rChild == NULL)
				return -1;
			q = q->rChild;
		}
	}
}
void insertItem(NODE *w, int k) {
	NODE *l,*r; getNode(&l); getNode(&r);
	NODE *p = treeSearch(w, k); p->key = k;
	p->lChild = l;p->rChild = r;
	l->parent = p;r->parent = p;
}
int removeElement(NODE *w, int k) {
	NODE *p = treeSearch(w, k), *z, *y;
	int key=p->key;
	if (isExternal(p))
		return -1;
	if (isInternal(p->lChild))
		z = p->rChild;
	else
		z = p->lChild;
	if (isExternal(z))
		reduceExternal(w,z);
	else {
		y = inOrderSucc(p); //p의 후계자
		z = y->lChild; 
		p->key = y->key; //값 넣어주기
		reduceExternal(w,z); //z와 z의 부모노드는 함께 사라짐
	}
	return key;
}
void printnode(NODE *w) {
	if (isExternal(w))
		return;
	else {
		printf(" %d", w->key);
		printnode(w->lChild);
		printnode(w->rChild);
	}
}
