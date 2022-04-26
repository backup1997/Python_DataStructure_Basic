class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # 槽，保存key，哈希处理
        self.datas = [None] * self.size

    # hash函数就是简单的求余
    def hashfunction(self, key):
        return key % self.size

    # 冲突的解决采用线性探测
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size  # 加1以重新散列

    def put(self, key, data):
        hashvalue = self.hashfunction(key)  # 求散列值
        # key不存在，未冲突
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.datas[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.datas[hashvalue] = data  # key已存在，替换val
            else:  # 散列冲突，再散列，直至找到空槽或key
                # foundNew = False
                # oldhashvalue = hashvalue
                # while not foundNew:
                #     rehashvalue = self.rehash(oldhashvalue)
                #     if self.slots[rehashvalue] is None:
                #         self.slots[rehashvalue] = key
                #         self.slots[rehashvalue] = data
                #         foundNew = True
                #     else:
                #         oldhashvalue = rehashvalue
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.datas[nextslot] = data
                else:
                    self.datas[nextslot] = data

    def get(self, key):
        # startslot标记为查找起点
        startslot = self.hashfunction(key)
        data = None
        stop = False  # 用以标记是否回到起点
        found = False
        position = startslot
        # 找key，直至空槽或回到起点
        # while not found and not stop: 缺少了空槽判断
        while self.slots[position] is not None and not found and not stop:
            # 未找到key，再散列继续找
            if self.slots[position] != key:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
            else:
                data = self.datas[position]
                found = True
        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key,value)
