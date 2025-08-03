#Viết CT nhập số tự nhiên n, kiểm tra nếu n là hợp số thì phân tích thành các thừa số nguyên tố (số 1 không là số nguyên tố & cũng không là hợp sô)


#hàm kiểm tra nguyên tố
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


# print(prime(111))

#Hàm phân tích hợp số thành thừa số nguyên tố
def factorize(n):
    i=2
    factors=[]
    while i*i<=n:   
        while n%i==0:
            factors.append(i)
            n=n//i
        i+=1
    
    #Sau vòng lặp có thể sót lại thừa số nguyên tố lớn hơn sqrt(n)
    if n>1:
        factors.append(n)
    
    return factors

#Nhập n 
while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Không hợp lệ.')
    except ValueError:
        print('Không hợp lệ')

if prime(n):
    print(f'{n} là số nguyên tố.')
elif n>1:
    print(f'{n} là hợp số.')
    factors=factorize(n)
    print(f'{n}=','x'.join(map(str,factors)))
