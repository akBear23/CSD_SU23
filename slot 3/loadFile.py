while(True):
    try:
        fileName = input('Nhap ten file/ duong dan: ')
        f = open(fileName, 'r')
        lst = f.readlines()
        for student in lst:
            print(student, end='')
        break
    except Exception as e:
        print(e)