from NodeLinkedTree import BinaryTree


def preorderTraverse(eTree):
    if eTree:
        print(eTree.getRootVal())
        preorderTraverse(eTree.getLeftChild())
        preorderTraverse(eTree.getRightChild())


def inorderTraverse(eTree):
    if eTree:
        inorderTraverse(eTree.getLeftChild())
        print(eTree.getRootVal())
        inorderTraverse(eTree.getRightChild())


def postorderTraverse(eTree):
    if eTree:
        postorderTraverse(eTree.getLeftChild())
        postorderTraverse(eTree.getRightChild())
        print(eTree.getRootVal())

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
preorderTraverse(r)