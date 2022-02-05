#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
typedef struct node {
	struct node *lChild;
	struct node *rChild;
	struct node *parent;
	int key;
	int height;
}NODE;
void getNode(NODE **p) {
	(*p) = (NODE *)malloc(sizeof(NODE));
	(*p)->lChild = NULL;
	(*p)->parent = NULL;
	(*p)->rChild = NULL;
}
NODE *root;
int isExternal(NODE *w);
int isInternal(NODE *w);
NODE *sibling(NODE *w);
NODE *inOrderSucc(NODE *w);
void printnode(NODE *w);
NODE *treeSearch(NODE *w, int k);
int findElement(NODE *w, int k);
void expandExternal(NODE *w);
void insertItem(NODE *t, int k);
void searchAndFixAfterInsertion(NODE *w);
int removeElement(NODE *w, int k);
NODE *reduceExternal(NODE *z);
void searchAndFixAfterRemoval(NODE *z);
int updateHeight(NODE *w);
int isBalanced(NODE *w);
NODE *restructure(NODE *x, NODE *y, NODE *z);
int main() {
	getNode(&root);
	char ch;
	int k, l;
	while (1) {
		scanf("%c", &ch);getchar();
		if (ch == 'i') {
			scanf("%d", &k);getchar();
			insertItem(root, k);
		}
		else if (ch == 's') {
			scanf("%d", &k);getchar();
			l = findElement(root, k);
			if (l == -1)
				printf("X\n");
			else
				printf("%d\n", l);
		}
		else if (ch == 'p') {
			printnode(root);
			printf("\n");
		}
		else if (ch == 'd') {
			scanf("%d", &k);getchar();
			l = removeElement(root, k);
			if (l == -1)
				printf("X\n");
			else
				printf("%d\n", l);
		}
		else
			break;
	}
	return 0;
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
void printnode(NODE *w) {
	if (isExternal(w))
		return;
	else {
		printf(" %d", w->key);
		printnode(w->lChild);
		printnode(w->rChild);
	}
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
void expandExternal(NODE *w) {
	NODE *l, *r;
	getNode(&l);getNode(&r);
	l->parent = w;r->parent = w;
	l->height = 0;r->height = 0;
	w->lChild = l;w->rChild = r;
	w->height = 1;
	return;
}
void insertItem(NODE *t, int k) {
	NODE *w = treeSearch(t, k);
	if (isInternal(w)) //이미 존재
		return;
	else {
		w->key = k;
		expandExternal(w); //w에 외부노드 연결
		searchAndFixAfterInsertion(w); 
	}
}
void searchAndFixAfterInsertion(NODE *w) { 
	//균형검사를 수행하고 불균형이 있으면 개조를 통해 높이균형 속성을 회복
	NODE *z, *y, *x;
	if (w->parent == NULL)
		return;
	z = w->parent;
	while (updateHeight(z) && isBalanced(z)) {
		if (z->parent == NULL)
			return;
		z = z->parent;
	}
	if (isBalanced(z))
		return;
	if (z->lChild->height > z->rChild->height)
		y = z->lChild;
	else
		y = z->rChild;
	if (y->lChild->height > y->rChild->height)
		x = y->lChild;
	else
		x = y->rChild;
	restructure(x, y, z);
	return;
}
int updateHeight(NODE *w) {
	int h;
	if (w->lChild->height > w->rChild->height)
		h = w->lChild->height + 1;
	else
		h = w->rChild->height + 1;
	if (h != w->height) {
		w->height = h;
		return 1;
	}
	else
		return 0;
}
int isBalanced(NODE *w) {
	int x;
	x = (w->lChild->height) - (w->rChild->height);
	if (x == -1 || x == 0 || x == 1)
		return 1;
	else
		return 0;
}
NODE *restructure(NODE *x, NODE *y, NODE *z) {
	NODE *a=NULL, *b=NULL, *c=NULL, *t0=NULL, *t1=NULL, *t2=NULL, *t3=NULL;
	if (z->key < y->key && y->key < x->key) {
		a = z;b = y;c = x;
		t0 = a->lChild;t1 = b->lChild;t2 = c->lChild;t3 = c->rChild;
	}
	else if (x->key < y->key && y->key < z->key) {
		a = x;b = y;c = z;
		t0 = a->lChild;t1 = a->rChild;t2 = b->rChild;t3 = c->rChild;
	}
	else if (z->key < x->key && x->key < y->key) {
		a = z;b = x;c = y;
		t0 = a->lChild;t1 = b->lChild;t2 = b->rChild;t3 = c->rChild;
	}
	else{
		a = y;b = x;c = z;
		t0 = a->lChild;t1 = b->lChild;t2 = b->rChild;t3 = c->rChild;
	}
	if (z->parent == NULL) {
		root = b;
		b->parent = NULL;
	}
	else if (z->parent->lChild == z) {
		z->parent->lChild = b;
		b->parent = z->parent;
	}
	else {
		z->parent->rChild = b;
		b->parent = z->parent;
	}
	a->lChild = t0;a->rChild = t1;
	t0->parent = a;t1->parent = a;
	updateHeight(a);
	c->lChild = t2;c->rChild = t3;
	t2->parent = c;t3->parent = c;
	updateHeight(c);
	b->lChild = a;b->rChild = c;
	a->parent = b;c->parent = b;
	updateHeight(b);
	return b;
}
NODE *reduceExternal(NODE *z) { //외부노드인 z넣고 , 사라지는 z의 부모노드 반환
	NODE *w = z->parent;  //z의 부모노드
	NODE *zs = sibling(z); //z의 형제 노드
	NODE *g;
	if (w->parent == NULL) { // z의 부모노드가 루트
		root = zs;
		zs->parent = NULL;
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
int removeElement(NODE *t, int k) {
	NODE *w = treeSearch(root, k), *z, *zs, *y;
	if (isExternal(w))
		return -1;
	z = w->lChild;
	if (!isExternal(z))
		z = w->rChild;
	if (isExternal(z))
		zs = reduceExternal(z);
	else {
		y = inOrderSucc(w);
		z = y->lChild;
		w->key = y->key;
		zs = reduceExternal(z);
	}
	searchAndFixAfterRemoval(zs->parent);
	return k;
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
void searchAndFixAfterRemoval(NODE *z) {
	NODE *y, *x, *b;
	while (updateHeight(z) && isBalanced(z)) {
		if (z->parent == NULL)
			return;
		z = z->parent;
	}
	if (isBalanced(z))
		return;
	if (z->lChild->height > z->rChild->height)
		y = z->lChild;
	else
		y = z->rChild;
	if (y->lChild->height > y->rChild->height)
		x = y->lChild;
	else if (y->lChild->height < y->rChild->height)
		x = y->rChild;
	else {
		if (z->lChild == y)
			x = y->lChild;
		else
			x = y->rChild;
	}
	b = restructure(x, y, z);
	if (b->parent == NULL)
		return;
	searchAndFixAfterRemoval(b->parent);
}
