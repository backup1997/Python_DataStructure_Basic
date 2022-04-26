from graph import Graph
from graph import Vertex


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
