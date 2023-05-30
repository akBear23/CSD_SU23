n = int(input('Nhap so n: '))
stack = []
while n != 0:
    stack.append(n%2)
    n = n//2

# print(stack)6
while(len(stack) > 0):
    print(stack.pop(), end='')