# 宝物的重量和价值
tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4},
      {'w': 4, 'v': 8}, {'w': 5, 'v': 8},
      {'w': 9, 'v': 10}
      ]
# 背包最大承重
max_w = 20

# 初始化二维表格m[(i,w)]
# 表示前i个宝物中，最大重量w的组合，所得到的最大价值
# 当i什么都不取，或w上限为0，价值均为0
m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}

# 逐个填写二维表格
for i in range(1, len(tr)):
    for w in range(1, max_w + 1):
        if tr[i]['w'] > w:  # 装不下第i个宝物
            m[(i, w)] = m[(i - 1, w)]  # 不装第i个宝物
        else:
            # 不装第i个宝物，装第i个宝物，两种情况下的最大价值
            m[(i, w)] = max(
                m[(i - 1, w)],
                m[(i - 1, w - tr[i]['w'])] + tr[i]['v']
            )
# 输出结果
print(m[(len(tr) - 1, max_w)])

# 下面是递归解法

# 宝物的重量和价值，tr是元组的集合
tr={(2,3),(3,4),(4,8),(5,8),(9,10)}
# 最大承重
max_w=20

# 初始化记忆化表格m,也就是备忘录
# key是(宝物组合，最大重量),value是最大价值
m={}

def thief(tr,w):
    if tr==set() or w==0: #如果没有宝物或者载重为0
        m[(tuple(tr),w)]=0 # tuple是key的要求，在备忘录记下
        return 0
    elif (tuple(tr),w) in m: #如果tr和w的组合在备忘录里，则直接返回
        return m[(tuple(tr),w)]
    else:
        vmax=0 # 最大价值初始化为0
        for t in tr:
            if t[0]<=w:
                # 逐个从集合种去掉某个宝物，递归调用
                # 选出所有价值种最大值
                v=thief(tr-{t},w-t[0])+t[1]  # 减小规模的调用
                vmax=max(vmax,v)
        m[(tuple(tr),w)]=vmax # vmax作为中间结果，保存到备忘录
        return vmax
# 输出结果
print(thief(tr,max_w))