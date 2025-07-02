#Năm n là năm nhuận nếu giá trị thỏa mãn: n chia hết cho 400 hoặc n chia hết cho 4 nhưng không chia hết 100. 
#Viết chương trình kiểm tra năm n có phải năm nhuận hay không

def namNhuan():
    while True:
        try:
            n = int(input('Nhập năm cần kiểm tra năm nhuận: '))
            if n <= 0: 
                print(f'Năm {n} không hợp lệ! Vui lòng nhập lại!') 
                continue 
            break
        except ValueError:
            print(f'Năm {n} không hợp lệ! Vui lòng nhập lại')
    if (n%400==0) or (n%4==0 and n%100!=0):
        return f'{n} là năm nhuận.'
    else:
        return f'{n} không phải năm nhuận.'

print(namNhuan())  
