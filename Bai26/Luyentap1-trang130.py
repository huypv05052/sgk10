#Viết hàm với tham số là số tự nhiên n in ra các số là ước nguyên tố của n


#Định nghĩa hàm kiểm tra nguyên tố trước
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

'''def uocNguyenTo(n):
    if n<1:
        return 'Đối số không hợp lệ.'

    print(f'Ước nguyên tố của {n} là: ')
    for i in range(1,n+1):
        if n%i==0:
            if prime(i):
                print(i, end=' ')
    print()

uocNguyenTo(10)
uocNguyenTo(360)
uocNguyenTo(20)'''


#Method 2:
def uocNguyenTo(n):
    if n<0:
        return 'Đối số không hợp lệ.'
    result=[]
    i=1
    while i<=n:
        if n%i==0 and prime(i):
            result.append(i)
        i+=1
    return f'Ước nguyên tố của {n} là: {result}'

print(uocNguyenTo(10))
