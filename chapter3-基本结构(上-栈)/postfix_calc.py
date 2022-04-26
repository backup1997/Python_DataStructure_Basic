from stack import Stack

# 可以把运算写成一个函数
# 更简便地使用eval(former+operation+latter)直接得到结果
def domath(op,num1,num2):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    else:
        return num1/num2

def postfixcalc(string):
    num_stack=Stack()
    pos=0
    length=len(string)
    while pos<length:
        if string[pos].isdigit():
            num_stack.push(string[pos])
        else:
            if string[pos]=="+":
                latter=int(num_stack.pop())
                former=int(num_stack.pop())
                num_stack.push(former+latter)
            elif string[pos]=="-":
                latter=int(num_stack.pop())
                former=int(num_stack.pop())
                num_stack.push(former-latter)
            elif string[pos] == "*":
                latter = int(num_stack.pop())
                former = int(num_stack.pop())
                num_stack.push(former * latter)
            else:
                latter = int(num_stack.pop())
                former = int(num_stack.pop())
                num_stack.push(former // latter)
        pos=pos+1
    return num_stack.pop()
print(postfixcalc("456*+"))