#Viết Ct nhập một string có thể có nhiều dấu cách giữa các từ. Sau đó chỉnh sửa xâu kí tự đó sao cho giữa các từ chỉ có một dấu cách. In xâu kết quả ra.

'''s=input('Nhập vào một string: ')
sub_s=s.split()         #Chuyển string ban đầu thành list
result=' '.join(sub_s)  #Nối các element trong list thành string bằng join
print(result)'''


def stringConect():
    while True:
        s=input('Nhập string: ')
        if s=='':
            print('Chưa nhập string.')
            continue
        break
    # print(s)
    sub_s=s.split()
    result=' '.join(sub_s)
    print(f'String kết quả: {result}')
stringConect()           
