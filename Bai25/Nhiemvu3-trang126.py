#Viết CT nhập số tự nhiên n, rồi nhập họ tên của n học sinh. In ra danh sách tên học sinh theo 2 cột, cột tên và cột họ đệm

while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập n nguyên dương.')
    except ValueError:
        print('Nhập n nguyên dương.')

lstName=[]
for i in range(n):
    while True:
        name=input(f'Nhập họ và tên học sinh thứ {i+1}: ').strip()
        if not name:
            print('Chưa nhập họ tên.')
        elif any(k.isdigit() for k in name):
            print('Tên mà chứa số.')
        else:
            lstName.append(name)
            break

# for i,val in enumerate(lstName):
#     print(f'{i+1}. {val}')

print('TÊN - HỌ ĐỆM: ')
for i in lstName:
    tach_ten=i.split()
    lastName=tach_ten[-1]
    middleName=' '.join(tach_ten[1:-1])
    if middleName=='':
        middleName='[Không có]'
    print(f'{lastName} - {middleName}')
