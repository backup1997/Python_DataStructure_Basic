def toStr(num, base):
    convertString = "0123456789ABCDEF"  # 支持2~16进制转换
    if num < base:  # 小于最小基
        return convertString[num]  # @=最小规模
    else:  # 减小规模，调用自身
        return toStr(num // base, base) + convertString[num % base]


print(toStr(21, 16))
