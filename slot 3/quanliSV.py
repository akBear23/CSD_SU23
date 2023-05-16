f = open('Data.txt', 'w')
while(True):
    ID = input('Nhap ma sinh vien: ')
    name = input('Nhap ten sinh vien: ')
    mark = input('Nhap diem sinh vien: ')

    f.write('{} {} {} \n'.format(ID, name, mark))   #ghi vao file theo format
    flag = input('Ban co tiep tuc muon nhap thong tin sinh vien [C/K]: ')
    flag = flag.lower()         #chuan hoa du lieu nhap vao 
    if(flag == 'k'): break      #dung nhap