from graph import Graph


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


def genLegalMoves(x, y, bdsize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]  # 马走日八个格子
    for offset in moveOffsets:
        newX = x + offset[0]
        newY = y + offset[1]
        if legalCoord(newX, bdsize) and legalCoord(newY, bdsize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdsize):  # 确认不会走出棋盘
    if x >= 0 and x < bdsize:
        return True
    else:
        return False


def knightGraph(bdsize):
    """
    :param bdsize: 棋盘的长度，标准国际象棋是500
    :return: 建立骑士周游图
    """
    ktGraph = Graph()
    for row in range(bdsize):  # 遍历每个格子
        for col in range(bdsize):
            nodeID = row * bdsize + col
            newPositions = genLegalMoves(row, col, bdsize)  # 单步合法走棋
            for edge in newPositions:
                newID = edge[0] * bdsize + edge[1]
                ktGraph.addEdge(nodeID, newID)  # 添加边及顶点
    return ktGraph


graph = knightGraph(8)


def knightTour(n, path: Stack, node: Vertex, limit):
    """
    :param n:当前层次
    :param path: 一个栈，保存着路径
    :param u:当前顶点
    :param limit:搜索总深度/节点总数
    """
    node.setColor("Grey")  # 当前节点设置颜色后加入路径
    path.push(node)
    if n < limit:
        nbrlist = list(node.getConnections())  # 对所有的合法路径逐一深入
        i = 0
        done = False
        while i < len(nbrlist) and not done:  # 选择白色且未经过的顶点深入
            if nbrlist[i].getColor == "White":
                done = knightTour(n + 1, path, nbrlist[i], limit)  # 层次加1，递归深入
            i = i + 1  # 如果没有找到，递归的done值为False，则选择同一层的下一个节点继续探测
        if not done:  # 对所有的邻居，有无法完成总深度，回溯，尝试本层下一个顶点
            path.pop()
            node.setColor("White")
    else:
        done = True
    return done
