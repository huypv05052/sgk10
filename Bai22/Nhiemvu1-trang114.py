#NV1: Nhập danh sách n tên học sinh trong lớp, in ra danh sách tên đó, mỗi tên trên 1 dòng
n = int(input('n='))
ten = []
for i in range(1, n+1):
    ten.append(input(f'Tên hs thứ {i}: '))
# print(ten)
for i in range(n):
    print(f'{i+1}. {ten[i]}')





Note: Kiểm soát dữ liệu vào, không nhập lung tung
while True:
    try:
        n=int(input('n='))
        if n > 0:
            break
        else:
            print('Số học sinh phải là số nguyên dương!')
    except ValueError:
        print('Số học sinh phải là số nguyên dương!')
    
ten = []
for i in range(1, n+1):
    while True:
        tenhs = input(f'Nhập tên học sinh thứ {i}: ')
        if tenhs == '':
            print('Tên không được để trống!')
        elif any(char.isdigit() for char in tenhs):
            print('Tên không được chứa số!')
        elif tenhs[0] == ' ':
            print('Ký tự đầu không được là dấu cách!')
        else:
            ten.append(tenhs)
            break

for i in ten:
    print(i)



def dsTen():
    while True:
        try: 
            n=int(input('n='))
            if n>0:
                break
            else:
                print('Số học sinh phải là số nguyên dương.')
        except ValueError:
            print('Số học sinh phải là số nguyên dương.')

    ten=[]
    for i in range(1, n+1):
        while True:
            tenhs=input(f'Nhập tên học sinh thứ {i}: ')
            if tenhs[0]==' ':
                print('Ký tự đầu không được để trống!')
            elif tenhs=='':
                print('Không được để trống!')
            elif any(char.isdigit() for char in tenhs):
                print('Không được chứa số.')
            else:
                ten.append(tenhs)
                break
    print('Danh sách tên học sinh đã nhập:')
    for i in range(len(ten)):
        print(f'{i+1}. {ten[i]}')

dsTen()
