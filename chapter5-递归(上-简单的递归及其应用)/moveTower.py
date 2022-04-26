def moveTower(height, fromPole, withPole, toPole):
    """
    :param height: 汉诺塔高度
    :param fromPole: 1#柱子
    :param withPole: 2#柱子
    :param toPole: 3#柱子
    :return:
    """
    if height >= 1:  # 基本结束条件，height<1什么都不做
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)  # 把最大的height盘从fromPole挪动到toPole
        moveTower(height - 1, withPole, fromPole, toPole)


def moveDisk(disk, fromPole, toPole):
    """
    :param disk: 盘的高度号,最上面是1号盘
    :param fromPole: 起始柱子
    :param toPole: 最终柱子
    :return:
    """
    print(f"moving disk[{disk}] from {fromPole} to {toPole}")

moveTower(64,"#1","#2","#3")