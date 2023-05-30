tickets = int(input('Nhap so ve: '))
queue = []

n = int(input('Nhap so luong nguoi: '))

for i in range(n):
    name = input('Nhap ten: ')
    ticket = int(input('Nhap so ve: '))
    queue.append(ticket)

while(tickets > 0 or len(queue) > 0):
    x = queue.pop(0)
    if(tickets > x): print(x)
    else: print(tickets)
    tickets -= x

while(len(queue) > 0):
    print(0)