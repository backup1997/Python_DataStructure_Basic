def recDC(coinValueList, change, knownResults):
    """
    优化后的递归找零问题，增加了knownResults记录中间结果
    :param coinValueList:币值序列
    :param change:零钱
    :param knownResults:已知的计算结果，初值为0*change
    :return:最少硬币数
    """
    minCoins = change
    if change in coinValueList:  # 递归记录结束条件
        knownResults[change] = 1  # 记录最优解
        return 1
    elif knownResults[change] > 0:  # 查表成功，使用最优解
        return knownResults[change]
    for i in [c for c in coinValueList if c <= change]:
        numCoins = 1 + recDC(coinValueList, change - i, knownResults)
        if numCoins < minCoins:
            minCoins = numCoins
            # 找到最优解，记录到表中
            knownResults[change] = minCoins
    return minCoins


# 因为63需要记录0-64的最值，所以knownResults比change大1
print(recDC([1, 5, 10, 20, 21], 63, [0] * 64))
