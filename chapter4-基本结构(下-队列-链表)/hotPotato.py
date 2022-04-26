from queue_own import Queue_own


def hotPotato(namelist, num):
    user_queue = Queue_own()  # 创建一个队列
    for name in namelist:  # 玩家名字入队
        user_queue.enqueue(name)
    while user_queue.size() > 1:
        for i in range(num):  # 进行传递num次，传递过程通过将出队的元素入队来实现
            user_queue.enqueue(user_queue.dequeue())
        user_queue.dequeue()  # 每num次传递，出队一个玩家
    return user_queue.dequeue()  # 最后剩余的一个元素，即时赢家


namelist = ["Alice", "Bob", "Tom", "Jerry", "SonGoku", "Gane", "Mike"]
print(hotPotato(namelist, 2))
