#Viết CT nhập n họ tên học sinh. Yêu cầu nhập một tên và thông báo số đứa có cùng tên đó trong lớp

while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập n nguyên dương.')
    except ValueError:
        print('Nhập n nguyên dương.')

dsHoTen=[]
for i in range(n):
    while True:
        hoTen=input(f'Nhập họ tên học sinh thứ {i+1}: ').strip()
        if hoTen=='':
            print('Chưa nhập gì. Nhập đi.')
        elif any(k.isdigit() for k in hoTen):
            print('Tên mà chứa số. Nhập lại đi.')
        else:
            dsHoTen.append(hoTen)
            break
# print(dsHoTen)

tenCanTim=input('Nhập tên cần tìm: ').strip().lower()
count=0
for hoTen in dsHoTen:
    ten=hoTen.strip().split()[-1].lower()   #Lấy từ cuối cùng là tên
    if ten==tenCanTim:
        count+=1
if count:
    print(f'Có {count} học sinh có tên {tenCanTim.capitalize()}')
else:
    print(f'Không có học sinh tên {tenCanTim.capitalize()}')
