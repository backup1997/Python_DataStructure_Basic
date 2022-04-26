def sequentialSearch(numlist,item):
    for i in range(len(numlist)):
        if numlist[i]==item:
            return i
    return None

# 老师的写法,依旧是一个found标记和pos位置标记
def sequentialSearchUp(alist,item):
    pos=0
    found=False
    while pos <len(alist) and not found:
        if alist[pos]==item:
            found=True
        pos=pos+1
    return found

def orderedsequentialSearch(alist,item):
    pos=0
    found=False
    stop=False
    while pos < len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
        else:
            if item<alist[pos]:
                stop=True
            else:
                pos=pos+1
    return found
testlist=[0,1,4,5,7,11,41,51]
print(orderedsequentialSearch(testlist,3))
print(orderedsequentialSearch(testlist,11))