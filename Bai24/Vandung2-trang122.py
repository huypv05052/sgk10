#Viết CT nhập số học sinh và họ tên học sinh. Sau đó đếm xem trong danh sách có bao nhiêu đứa tên 'Hương'


def checkName():
    while True:
        try:
            n=int(input('n='))
            if n>0:
                break
            else:
                print('Nhập n nguyên dương.')
        except ValueError:
            print('Nhập n nguyên dương.')

    dsTen=[]
    for i in range(n):
        while True:
            ten=input(f'Nhập họ và tên học sinh thứ {i+1}: ').strip() #strip loại bỏ cách đầu và cuối
            if not ten:
                print('Chưa nhập họ và tên.')
            elif any(k.isdigit() for k in ten):
                print('Không được nhập số.')
            else:
                dsTen.append(ten)
                break
    print('Danh sách họ và tên vừa nhập:')
    for i,val in enumerate(dsTen):
        print(f'{i+1}. {val}')

    #Kiểm tra có đứa nào tên 'Hương':
    count_huong=0
    for name in dsTen:
        name=name.strip()                   #Xóa cách đầu và cuối tên
        tach_name=name.split()              #tách tên thành các từ
        last_name=tach_name[-1]             #Lấy tên thôi
        if last_name.lower()=="hương":      #Lower để không phân biệt chữ hoa và thường
            count_huong+=1
    if count_huong>0:
        print(f'Có {count_huong} đứa tên Hương trong danh sách.')
    else:
        print('Không có ai tên Hương.')

checkName()
