#Viết chương trình nhập họ tên đầy đủ của người dùng, sau đó in thông báo tên và họ đệm của người đó


'''while True:
    ho_ten=input('Nhập họ và tên: ')
    if ho_ten=="":
        print('Chưa nhập họ và tên.')
        continue
    
    lst=ho_ten.split()
    if len(lst)<2:
        print('Vui lòng nhập đầy đủ họ và tên.')
        continue
    break

ho=lst[0]
ten=lst[-1]
ho_dem=' '.join(lst[1:-1])          #Lấy phần từ thứ 2 tới phần tử áp chót

print(f'Tên đã nhập: {ten}')
print(f'Họ đệm tên đã nhập: {ho_dem}')'''


def hoTen():
    while True:
        full_name=input("Nhập họ và tên: ")
        if full_name=='':
            print('Chưa nhập họ tên.')
            continue
        
        lst=full_name.split() #Tách họ tên thành list các từ
        if len(lst)<2:
            print('Nhập đầy đủ họ tên.')
            continue
        break

    first_name=lst[0]
    last_name=lst[-1]
    middle_name=' '.join(lst[1:-1])
    if middle_name=='':
        print('Không có họ đệm.')
    else:
        print(f'Họ đệm: {middle_name}')
    print(f'Tên: {last_name}')

hoTen()
