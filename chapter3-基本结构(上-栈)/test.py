from stack import Stack,Stack_two

#stack_1=Stack #类赋值，错误的，应该是对象。
stack_2=Stack_two()
print(stack_2.isEmpty())

stack_2.push('a')
stack_2.push(1)
print(stack_2.peek())
print(stack_2.pop())
print(stack_2.pop())
