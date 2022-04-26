# 解法1:两重循环法，对第一个序列中的每个，对第二个字符串遍历 O(n^2)
def anagram1(s1, s2):
    list_s2 = list(s2)
    for pos1 in range(len(s1)):
        flag = 0
        for pos2 in range(len(s2)):  # 两重判断，保证找到就打勾并退出来，而不是一直循环
            if s1[pos1] == list_s2[pos2]:
                flag = 1
                list_s2[pos2] = None
                break
        if flag == 0:
            return False
    return True


# 解法2:先排序，后比较 排序的时间复杂度是O(N*logN)
def anagram2(s1, s2):
    list_s1 = list(s1)
    list_s2 = list(s2)
    list_s1.sort()
    list_s2.sort()
    for pos in range(len(s1)):
        if list_s1[pos] != list_s2[pos]:
            return False
    return True


# 解法3:统计词频，空间换时间，比较词频，如果一致则是同位词 O(2n+26)
def anagram3(s1, s2):
    dict_s1 = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    dict_s2 = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
        'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
        'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
        'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    # 默认输入的全是小写
    for chr_s1 in s1:
        dict_s1[chr_s1] = dict_s1[chr_s1] + 1
    for chr_s2 in s2:
        dict_s2[chr_s2] = dict_s2[chr_s2] + 1
    for i in range(97, 123): # 从a到z
        char = chr(i)
        if dict_s1[char] != dict_s2[char]:
            return False
    return True


print(anagram3("typhon", "pzthon"))
