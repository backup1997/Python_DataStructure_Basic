from stack import Stack


def base_change(num):
    s = Stack()
    while num >= 1:
        factor = num % 2
        num = num // 2  # 注意这里必须整数除法，不然余数后来是小数
        s.push(factor)
    binstr = ""
    while not s.isEmpty():
        binstr = binstr + str(s.pop())
    return binstr



print(base_change(25))
print(baseConverter(25,16))