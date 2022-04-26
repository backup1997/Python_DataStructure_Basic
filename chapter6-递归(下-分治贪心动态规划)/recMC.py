def recMC(coinValueList, change):
    mincoins = change  # 最小硬币数目，计算过程中更新
    if change in coinValueList:
        return 1
    for i in [c for c in coinValueList if c <= change]:
        numCoins = 1 + recMC(coinValueList, change - i)
        if numCoins < mincoins:
            mincoins = numCoins
    return mincoins


print(recMC([1, 5, 10, 20, 21], 63))
