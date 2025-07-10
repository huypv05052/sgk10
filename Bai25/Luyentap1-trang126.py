#Viết CT nhập nhiều số (nguyên hoặc thực), các số cách bởi dấu cách. In ra tổng các số đã nhập


while True:
    num_str=input('Nhập các số cách nhau bằng dấu cách: ').strip()
    if num_str=='':
        print('Nhập vài số chơi.')
        continue

    num_str_lst=num_str.split()
    # print(num_str_lst)


    '''try:
        tong=0
        for i in num_str_lst:
            tong+=float(i)
        print(f'Tổng các số trong string: {tong}')
        break
    except ValueError:
        print('Có phần tử không phải số. Nhập lại đi.')'''
    
    try:
        num_lst=[float(i) for i in num_str_lst]
        print(f'Tổng các số trong string: {sum(num_lst)}')
        break
    except ValueError:
        print('Có phần tử không phải số. Nhập lại đi.')
