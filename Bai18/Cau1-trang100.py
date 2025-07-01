#Viết chương trình nhập 3 số thực dương a, b, c và tính chu vi, diện tích tam giác có độ dài ba cạnh là a, b, c
# suggest: S = sqrt(p(p-a)(p-b)(p-c)) , p là nửa chu vi
# Method 1
import math
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

p = (a + b + c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'Chu vi tam giác bằng: {a+b+c}')
print(f'Diện tích tam giác bằng: {s}')


# Method 2
import math
def tamGiac():
    while True:
        try:
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))

            #check a, b, c is ok:
            if (a <= 0) or (b <= 0) or (c <= 0):
                print('Vui lòng nhập số thực dương!')
                continue
            if (a+b <= c) or (a+c <= b) or (b+c <= a):
                print('Ba cạnh không tạo thành tam giác hợp lệ! Vui lòng nhập lại!')
                continue
            break   #Dữ liệu hợp lệ! Thoát vòng lặp 
        except ValueError:
            print('Lỗi: Vui lòng nhập số thực!')

    #Tính chu vi, diện diện tích
    chu_vi = a+b+c
    p = chu_vi/2
    dien_tich = math.sqrt(p*(p-a)*(p-b)*(p-c))

    print(f'Chu vi tam giác bằng: {chu_vi}')
    print(f'Diện tích tam giác bằng: {dien_tich:.2f}')

tamGiac()
