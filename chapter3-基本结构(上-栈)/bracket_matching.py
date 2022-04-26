from stack import Stack

string = "((((())))"
s = Stack()
for str in string:
    if str == "(":
        s.push(str)
    elif str == ")":
        if s.isEmpty():
            print("error matching")
            exit(0)
        else:
            if s.peek() == "(":
                s.pop()
            else:
                print("error matching")
                exit(0)
if s.isEmpty():
    print("matching ok")
else:
    print("error matching")

# 实例化为一个函数，则需要返回true或false
# 更规范的，用while循环去索引字符串，且使用一个标记balanced去标记匹配情况
def brakcet_match(string):
    s=Stack()
    length=len(string)
    balanced=True
    index=0
    while index<length and balanced:
        symbol=string[index]  # 取单个字符,存储变量而不是每次调用字符串索引去计算，节省资源
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False