#Viết chương trình nhập số tự nhiên n là số học sinh, nhập họ tên học sinh. Lưu họ và tên học sinh vào một danh sách. In danh sách ra màn hình, mỗi họ tên trên một dòng


while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập n nguyên dương.')
    except ValueError:
        print('Nhập n nguyên dương.')

dsLop=[]
for i in range(n):
    ten=input(f'Nhập họ tên học sinh thứ {i+1}: ')
    dsLop.append(ten)
    
print('Danh sách học sinh: ')
for k in dsLop:
    print(k)
