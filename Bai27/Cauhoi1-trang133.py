#Dùng hàm prime, viết CT in ra các số nguyên tố trong khoảng từ m tới n
#Note: 1<m<n

def prime(n):
    if n<2:
        return False
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True

def printPrime(m,n):
    if not (1<m<n):
        return 'Đối số không hợp lệ.'
    
    '''print(f'Các số nguyên tố từ {m} tới {n} là: ')
    for i in range(m, n+1):
        if prime(i):
            print(i, end=' ')
    print()'''
    count=0
    primes=[]
    for i in range(m,n+1):
        if prime(i):
            primes.append(i)
            count+=1
    return f'Có {count} số nguyên tố từ {m} tới {n} là: {primes}'
    
print(printPrime(10, 4))
print(printPrime(4, 10))
print(printPrime(10, 30))
