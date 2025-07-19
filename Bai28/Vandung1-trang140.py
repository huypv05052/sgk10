#Viết hàm có hai tham số đầu vào là m,n. Đầu ra:
#Ước chung lớn nhất của 2 số
#Bội chung nhỏ nhất của 2 số.


#Hàm tìm ucln
def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a

#Hàm tìm BCNN
def bcnn(a,b):
    return abs(a*b)//ucln(a,b)


def main():
    while True:
        number=input('Nhập 2 số cách nhau bởi dấu cách: ').split()
        if len(number)!=2:
            print('Chưa hợp lệ.')
            continue
        
        try:
            num1, num2 = int(number[0]), int(number[1])
            if num1==0 and num2==0:
                print('Chưa hợp lệ.')
                continue
            break
        except ValueError:
            print('Chưa hợp lệ.')
            
    print(f'UCLN({num1},{num2})={ucln(num1,num2)}')
    print(f'BCNN({num1},{num2})={bcnn(num1,num2)}')
    

main()
