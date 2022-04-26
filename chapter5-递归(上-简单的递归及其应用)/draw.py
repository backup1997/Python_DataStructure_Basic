import turtle


def drawSprial(t, lineLen):
    if lineLen > 0:  # 最小规模
        t.forward(lineLen)
        t.right(90)
        drawSprial(t, lineLen - 1)  # 减小规模，调用自身


def tree(branch_len):
    if branch_len > 5:  # 树干太短不画，即递归结束条件
        t.forward(branch_len)  # 画树千
        t.right(20)  # 右倾斜28度
        tree(branch_len - 15)  # 递归调用，画右边的小树，树千减15
        t.left(40)  # 向左回40度，即左倾斜20度
        tree(branch_len - 15)  # 递归调用，画左边的小树，树干减15
        t.right(20)  # 向右回20度，即回正
        t.backward(branch_len)  # 海龟退回原位置


# drawSprial(t, 100)
# turtle.done()
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(150)  # 画树干长度75的二叉树
t.hideturtle()
turtle.done()
