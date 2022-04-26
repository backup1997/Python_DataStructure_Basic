from NodeLinkedTree import BinaryTree


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


# 有左右括号版本的语法解析树
def buildParseTree(sentence):
    tokens = list(sentence)
    pStack = Stack()
    emptyTree = BinaryTree('')
    pStack.push(emptyTree)  # 入栈下降
    currentTree = emptyTree
    # 表达式开始
    for token in tokens:
        # 入栈下将
        if token == "(":
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        # 出栈上升
        elif token == ")":
            currentTree = pStack.pop()
        # 操作符，设置值添加右节点，下降
        elif token in "+-*/":
            currentTree.setRootVal(token)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        # 操作数，设置值，出栈上升
        else:
            currentTree.setRootVal(int(token))
            currentTree = pStack.pop()
    return emptyTree


# def evaluate(parseTree):
#     if parseTree.getLeftChild() is None or parseTree.getRightChild() is None:
#         return parseTree.getRootVal()
#     else:
#         leftVal=evaluate(parseTree.getLeftChild())
#         rightVal=evaluate(parseTree.getRightChild())
#         parseTree.setRootVal(eval(str(leftVal)+str(parseTree.getRootVal())+str(rightVal)))
#         return parseTree.getRootVal()

import operator


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv
             }
    leftC = parseTree.getLeftChild()  # 缩小规模
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]  # 递归调用
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()  # 基本结束条件



# 下面是采用后序遍历法重写表达式代码：左/右/根
def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv
             }
    res1 = None
    res2 = None
    if tree:
        # 左子树
        res1 = postordereval(tree.getLeftChild())
        # 右子树
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()][res1, res2]
        else:  # 根节点
            return tree.getRootVal()

# 给树中节点生成全括号表达式
def printexp(tree):
    sVal=""
    if tree:
        if str(tree.key).isdigit():  #如果根是数值，即不是运算符，则必然没有表达式
            return str(tree.key)
        else:
            sVal="("+printexp(tree.getLeftChild())
            sVal=sVal+str(tree.getRootVal())
            sVal=sVal+printexp(tree.getRightChild())+")"
    return sVal

sentence = "(1+(3*4))"
eTree = buildParseTree(sentence)
eTree.inorder()
# print(evaluate(eTree))
print(printexp(eTree))