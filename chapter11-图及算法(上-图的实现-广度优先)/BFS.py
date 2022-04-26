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


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):  # 新加顶点
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):  # 通过key查找顶点
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, item):  # contains特殊方法，in操作
        return item in self.vertList

    def addEdge(self, fromVertex, toVertex, weight=0):
        if fromVertex not in self.vertList:  # 不存在的顶点先添加
            newVertex = self.addVertex(fromVertex)
        if toVertex not in self.vertList:
            newVertex = self.addVertex(toVertex)
        self.vertList[fromVertex].addNeighbor(self.vertList[toVertex], weight)  # 调用起始顶点的方法添加邻接边，注意添加的值是vertex类型的

    def getVertices(self):
        return self.vertList.keys()  # 将所有顶点作为列表返回

    def __iter__(self):  # 特殊方法，迭代函数，实现了可以用for迭代取出顶点的操作
        return iter(self.vertList.values())


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # 因为要添加该顶点连接的其他边，及其上权重信息，所以是字典类型
        self.distance = None
        self.color = "White"  # 初始没有访问过，颜色为默认的白色
        self.pred = None  # 该节点的前驱，用以回溯

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):  # 字符串化特殊方法，这样在print一个v顶点的时候，就可以以这样的方式把顶点打印出来
        return str(self.id) + 'connectedTo: ' + str(x.id for x in self.connectedTo)

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setPred(self, vertex):
        self.pred = vertex

    def getPred(self):
        return self.pred

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def getConnections(self):  # 得到连接的其他顶点的key值，而不是vertex
        return self.connectedTo.keys()

    def getId(self):  # 返回key
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]  # 返回与nbr之间的连线的权重


def bfs(g, start):
    """
    进行一次广度优先遍历，为每个初始颜色为white的节点设置其pred和distance
    :param g:图
    :param start:起始节点
    """
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue_own()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()  # 取队首作为当前节点
        for nbr in currentVert.getConnections():  # 遍历队首节点的邻接节点
            #nbr=g.getVertex(nbr_key)  # 由key得到vertex
            if nbr.getColor() == "White":
                nbr.setColor("Gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor("Black")  # 当前顶点设置为黑色，就不再进行探索


def traverse(y):  # 从y节点回溯，找到其所有前驱节点
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())  # y的起始start

def buildGraph(wordFile):  # 以单词文件作为参数
    d = {}  # 存放单词桶与单词list的键值关系对
    g = Graph()
    wfile = open(wordFile, 'r')
    # 建桶
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):  # 4字母单词可属于4个桶
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)  # 有这个桶，向单词列表里添加单词即可
            else:
                d[bucket] = [word]  # 没有这个桶，创建仅包含一个word的list作为值
    # 同一个桶里面单词间添加边
    for bucket in d.keys():
        for word1 in d[bucket]:  # d[bucket]取这个桶里面的单词序列
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

wordgraph=buildGraph("./fourletterwords.txt")
#start=wordgraph.getVertex("FOOL")  # getVertex返回的确实是一个节点vertex
bfs(wordgraph,wordgraph.getVertex("FOOL"))
#end=wordgraph.getVertex("SAGE")
traverse(wordgraph.getVertex("SAGE"))