def dpMakeChange(coinValueList, change, minCoins):
    # 从1分钱开始到change逐个计算虽少硬币数
    for cents in range(1, change + 1):
        # 1.初始化一个最大值
        coinCount = cents
        # 2.减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= change]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
            # 3.得到当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
    return minCoins[change]


def dpMakeChangeUp(coinValueList, change, minCoins, coinUsed):
    """
    能够输出选取币值的升级版找零钱
    :param coinValueList: 硬币值体系
    :param change: 零钱
    :param minCoins: 最小硬币值 备忘录
    :param coinUsed: 每个零钱值下首先选取的币值
    :return:change零钱的最小硬币数
    """
    for cents in range(1, change + 1):
        coinCount = cents  # coinCount最终记录最小值，初始化为最大值
        newCoin = 1  # 初始化一下新硬币，其币值初始化为1
        for j in [c for c in coinValueList if c <= change]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j  # 当前对应的最小值，所减的硬币的币值
        minCoins[cents] = coinCount  # coinCount记录着最小值
        coinUsed[cents] = newCoin  # newCoin记录着选取的币值
    printCoins(coinUsed,change)
    return minCoins[change]

def printCoins(coinsUsed,change):
    """
    将各个change下选择的钱币打印出来
    :param coinsUsed: 各个change值下首选的币值
    :param change:change值
    """
    while change!=0:
        print(coinsUsed[change])
        change=change-coinsUsed[change]

print(dpMakeChange([1, 5, 10, 21, 25], 63, [0] * 64))
print(dpMakeChangeUp([1, 5, 10, 21, 25], 63, [0] * 64,[0]*64))
