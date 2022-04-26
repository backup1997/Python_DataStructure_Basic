from deque import Deque
def palcchecker(string):
    chardeque=Deque()
    for char in string:
        chardeque.addRear(char)
    match=True
    while not chardeque.size()>1 and match: #只有两个及两个以上，才判断
        frontChar=chardeque.removeFront()
        rearChar=chardeque.removeRear()
        if frontChar!=rearChar:
            match=False
    return match

print(palcchecker("shhhs"))