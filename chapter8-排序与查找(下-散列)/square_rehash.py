def squareHash(num,hashtable):
    base=len(hashtable)
    square_num=num*num
    str_num=str(square_num)
    mid=len(str_num)//2
    hashvalue=(int(str_num[mid])*10+int(str_num[mid+1]))%base
    if hashtable[hashvalue]==0:
        hashtable[hashvalue]=num
    else:
        newhashvalue=rehash(hashvalue,1,hashtable)
        hashtable[newhashvalue]=num
    return hashtable

def rehash(oldhashvalue,skip,hashtable):
    newhash=False
    while not newhash:
        newhashvalue=(oldhashvalue+skip)%len(hashtable)
        if hashtable[newhashvalue]==0:
            newhash=True
        else:
            skip=skip+1
    return newhashvalue

print(squareHash(113,[1,0,0,0]))
