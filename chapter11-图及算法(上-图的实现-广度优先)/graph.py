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
        self.vertList[fromVertex].addNeighbor(toVertex, weight)  # 调用起始顶点的方法添加邻接边

    def getVertices(self):
        return self.vertList.keys()  # 将所有顶点作为列表返回

    def __iter__(self):  # 特殊方法，迭代函数，实现了可以用for迭代取出顶点的操作
        return iter(self.vertList.values())


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # 因为要添加该顶点连接的其他边，及其上权重信息，所以是字典类型

    def addNeighbor(self, key, weight=0):
        self.connectedTo[key] = weight

    def __str__(self):  # 字符串化特殊方法，这样在print一个v顶点的时候，就可以以这样的方式把顶点打印出来
        return str(self.id) + 'connectedTo: ' + str(x.id for x in self.connectedTo)

    def getConnections(self):  # 得到连接的其他顶点
        return self.connectedTo.keys()

    def getId(self):  # 返回key
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]  # 返回与nbr之间的连线的权重
