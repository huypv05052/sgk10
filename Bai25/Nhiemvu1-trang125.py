#Viết Ct nhập nhiều số nguyên từ bàn phím, các số cách nhau bởi dấu cách. Khi nhập xong thông báo số lượng các số đã nhập và in ra các số thành 1 hàng ngang
#Gợi ý: Dữ liệu nhập vào là một xâu. Dùng lệnh split() tách thành danh sách. Chuyển các phần tử của danh sách này thành số và in ra màn hình.


'''numbers=input('Nhập các nguyên cách nhau bởi dấu cách: ')
num_str_lst=numbers.split()      #Lúc này num chuyển thành danh sách
print(num_str_lst)
n=len(num_str_lst)
lst_num=[]
for i in num_str_lst:
    lst_num.append(int(i))
print(f'Đã nhập {n} số: ')
for k in lst_num:
    print(k, end=' ')'''

'''def lstNum():
    numbers=input('Nhập các số nguyên cách nhau bởi dấu cách: ').strip()
    if numbers=='':
        print('Chưa nhập số nào, nhập vài số chơi.')
    else:
        num_str_lst=numbers.split()
        n=len(num_str_lst)      #n là số lượng số
        lst_num=[]              #lưu danh sách số
        for i in num_str_lst:
            lst_num.append(int(i))
        
        print("Các số đã nhập: ")
        for i in lst_num:
            print(i, end=' ')   
lstNum()     '''

# Yêu cầu phải nhập số, không được nhập ký tự khác
def lstNum():
    while True:
        numbers=input('Nhập các số cách nhau bởi dấu cách: ').strip()
        if numbers=='':
            print('Chưa nhập số nào, nhập vài số chơi.')
            continue

        num_str_lst=numbers.split()
        lst_num=[]

        check=True
        for i in num_str_lst:
            try:
                num=int(i)
                lst_num.append(num)
            except ValueError:
                print(f'{i} không phải số nguyên.')
                check=False
                break
        if check:
            break   #Dừng vòng lặp khi tất cả hợp lệ

    print('Các số đã nhập: ')
    for k in lst_num:
        print(k, end=' ')

lstNum()
