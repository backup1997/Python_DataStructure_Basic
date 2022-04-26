# def carpet(N,char):
#     if N==3: #最小问题
#         print(char*3+"\n")
#         print(char+" "+char+"\n")
#         print(char*3+"\n")
#     else:
def carpet(N, C):
    def check(n, x, y):
        if n <= 1:
            return True
        n2 = n // 3
        if n2 <= x < n2 * 2 and n2 <= y < n2 * 2:  # 在中间的部分，就挖掉
            return False  # 挖空的地方，不填
        return check(n2, x % n2, y % n2)  # 没有处于中间，递归调用

    for y in range(N):  # 对每一行，每一个点都检查并打印
        for x in range(N):
            if check(N, x, y):
                print(C, end='')
            else:
                print(' ' * len(C), end='')
        print('')  # 换行


carpet(27, '[]')
