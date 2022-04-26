import random
from queue_own import Queue_own
import time


class Printer:  # 打印机对象
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.currentTask = None  # 当前打印任务
        self.timeRemaining = 0  # 任务剩余时间/任务倒计时

    def tick(self):  # 打印1秒
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:  # 当前任务已经执行完
                self.currentTask = None

    def busy(self):  # 打印机忙？
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):  # 开始打印新作业
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() \
                             * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time  # 时间戳，记录生成时间
        self.pages = random.randint(1, 21)  # 打印页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):  # 等待时间
        return currentTime - self.timestamp


def newPrintTask():
    num = random.randrange(1, 181)  # 以1/180概率生成作业
    if num == 180:
        return True
    else:  # 其他179/180的情况不生成作业
        return False


def simulation(numSeconds, pagesPerMinute):
    # numSeconds模拟多长时间  pagesPerMinute，打印机的模式，每分钟打印多少页
    labprinter = Printer(pagesPerMinute)  # 生成一个打印机对象
    printQueue = Queue_own()  # 准备一个作业队列
    waitingtimes = []  # 各个作业的等待时间队列，以便最后统计

    for currentSecond in range(numSeconds):
        if newPrintTask():  # 有1/180的概率成立了，则生成打印作业
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            # 如果打印机不忙且打印队列不空，则可以继续打印任务
            nexttask = printQueue.dequeue()  # 取出一个打印任务
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()  # 打印一秒

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs and %3d tasks remaining" % (averageWait, printQueue.size()))


for i in range(10):
    simulation(3600, 5)  # 按5PPM,1小时的设定，模拟运行10次

for i in range(10):
    simulation(3600, 10)  # 按10PPM,1小时的设定，模拟运行10次
