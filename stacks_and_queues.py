names = ['knight', 'faith', 'charlo', 'verah']
stack =[]
#adding values in stack
for i in range(0, len(names)):
    stack.append(names[i])
    print(stack)
#removing itmes in stack
for i in range(0, len(names)):
    stack.pop()
    print(stack)
#updating values i  stack(list)
my_stack = [1,2,3,4,5,6,7,8,9,15]
def update(data, value):
    for i in range(0,len(my_stack)):
        if my_stack[i] == data:
            my_stack[i] = value
    return my_stack

update(4,12)