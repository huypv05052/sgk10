#Viết chương trình nhập n, tạo và in dãy số A gồm n số hạng đầu tiên của dãy Fibonacci
#Dãy Fibonacci: f0=0, f1=1, fn=fn-1+fn-2 (n>=2)


# def fibo(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

# print(fibo(10))


def fibo(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        f0,f1=0,1
        i=2
        while i<=n:
            f0,f1=f1,f0+f1
            i+=1
        return f1
# print(fibo(10))

def fiboLst():
    while True:
        try:
            n=int(input('n='))
            if n>0:
                break
            else:
                print('Nhập số nguyên dương.')
        except ValueError:
            print('Nhập số nguyên dương.')
    
    A=[fibo(i) for i in range(n)]
    print(f'{n} số hạng đầu tiên của dãy fibonacci: {A}')

fiboLst()
