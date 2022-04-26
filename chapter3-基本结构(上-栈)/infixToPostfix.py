from stack import Stack


def infixToPostfix(infixexpr):  # 中缀表达式转后缀表达式
    prec = {  # 优先级字典
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1  # 因为遇到左括号要继续压栈，左括号的优先级是最低的
    }
    opstack = Stack()  # 操作符栈
    postfix_list = []  # 后缀表达式串
    pos = 0
    length = len(infixexpr)
    while pos < length:  # 遍历取字符串中每个字符
        char = infixexpr[pos]
        if char == "(":
            opstack.push(char)
        elif char.isalpha() or char.isdigit():  # 如果是字母，则直接输出到后缀表达式栈
            postfix_list.append(char)
        elif char == ")":
            while opstack.peek() != "(":
                pop_char = opstack.pop()
                postfix_list.append(pop_char)
            opstack.pop()  # 将左括号弹栈
        else:
            if not opstack.isEmpty():
                while prec[opstack.peek()] >= prec[char]:
                    pop_char = opstack.pop()
                    postfix_list.append(pop_char)
            opstack.push(char)
        pos = pos + 1
    while not opstack.isEmpty():
        postfix_list.append(opstack.pop())
    postfix_string = "".join(postfix_list)
    return postfix_string

print(infixToPostfix("(A+B)*C"))
