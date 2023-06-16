hanghoa_file = open('slot 7\Hanghoa.txt', 'r')
khachhang_file = open('slot 7\Khachhang.txt', 'r')
mua_file = open('slot 7\Muaban.txt', 'r')

Hang = hanghoa_file.readlines()
Mahang = []
TenHang = []
Gia = []
for val in Hang:
    val = val.split(',')
    Mahang.append(val[0])
    TenHang.append(val[1])
    Gia.append(val[2])

Khach = khachhang_file.readlines()
# MaKhach = 



