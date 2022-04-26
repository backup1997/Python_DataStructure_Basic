class Stack:
    def __init__(self):
        self.items = []  # 自己取名为self.stack=[],视频里是self.items

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False
        # return self.items==[] 如上三行可以缩写为这样一行

    def push(self, param):
        self.items.append(param)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]  # 根据索引取值
        # return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Stack_two:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.insert(0, item)  # 时间复杂度为O(N)

    def pop(self):
        return self.items.pop(0)  # 时间复杂度为O(N)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
