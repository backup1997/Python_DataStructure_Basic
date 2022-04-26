class Queue_own:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def basesort(num_list, base):
    queue_main = Queue_own()
    queue_digits = []
    for i in range(base):
        queue_digits.append(Queue_own())
    max_num = max(num_list)
    for num in num_list:
        queue_main.enqueue(num)
    for i in range(max_num):  # 总共循环最大数的位数趟
        while not queue_main.isEmpty():
            pop_num = queue_main.dequeue()
            index = pop_num // pow(base, i) % base
            queue_digits[index].enqueue(pop_num)
        for j in range(0, base):  # 决定了排序顺序
            while not queue_digits[j].isEmpty():
                queue_main.enqueue(queue_digits[j].dequeue())
    ret_list = []
    while not queue_main.isEmpty():
        ret_list.append(queue_main.dequeue())
    return ret_list


print(basesort([88, 11, 5, 123, 44, 69, 71], 10))
