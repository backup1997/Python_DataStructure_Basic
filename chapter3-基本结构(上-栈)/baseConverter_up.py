#扩展到任意进制转换
def baseConverter(num,base):
    s=Stack()
    digits="0123456789ABCDEF"
    while num>=1:
        factor=num%base
        char=digits[factor]
        num=num//base
        s.push(char)
    newString=""
    while not s.isEmpty():
        newString=newString+s.pop()
    return newString