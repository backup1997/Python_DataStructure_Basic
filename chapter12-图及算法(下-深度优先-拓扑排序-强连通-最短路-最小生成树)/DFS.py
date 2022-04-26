from graph import Graph


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # 因为要添加该顶点连接的其他边，及其上权重信息，所以是字典类型
        self.distance = None
        self.color = "White"  # 初始没有访问过，颜色为默认的白色
        self.pred = None  # 该节点的前驱，用以回溯
        self.disc = 0  # 该节点的发现时间discovery
        self.fin = 0  # 该节点的结束探索时间finish

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

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getConnections(self):  # 得到连接的其他顶点的key值，而不是vertex
        return self.connectedTo.keys()

    def getId(self):  # 返回key
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]  # 返回与nbr之间的连线的权重


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()  # 调用父类的初始化
        self.time = 0

    def dfs(self):
        for aVertex in self:  # 颜色初始化
            aVertex.setColor('White')
            aVertex.setPred(-1)
        for aVertex in self:  # 如果还有未包括的顶点，则建森林
            if aVertex.getColor() == 'White':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex: Vertex):
        # 关键的深度优先搜索算法，创建单棵的深度优先树，是递归函数
        startVertex.setColor("Grey")
        self.time += 1  # 算法的步数
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            # 深度优先递归访问
            if nextVertex.getConnections():
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor("Black")  # 深度优先探索完毕后，当前节点颜色由灰色设为黑色
        self.time += 1
        startVertex.setFinish(self.time)
