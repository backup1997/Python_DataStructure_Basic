from stack import Stack


# 实例化为一个函数，则需要返回true或false
# 更规范的，用while循环去索引字符串，且使用一个标记balanced去标记匹配情况

def match(str_char, pop_char):
    str_chars = ")]}"  # 字符串中的应该是右符号
    pop_chars = "([{"  # 弹出来的因该是左符号
    return str_chars.index(str_char) == pop_chars.index(pop_char)


def brakcet_match(string):
    s = Stack()
    length = len(string)
    balanced = True
    index = 0
    while index < length and balanced:
        symbol = string[index]  # 取单个字符,存储变量而不是每次调用字符串索引去计算，节省资源
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                popchar = s.pop()  # 因为多了匹配字符，字符串中的要和栈中弹出来的相匹配，才正确
                if not match(symbol, popchar):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(brakcet_match("([{[()]})"))
