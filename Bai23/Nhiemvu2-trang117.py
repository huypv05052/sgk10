#Cho list A chứa số nguyên. Viết chương trình xóa đi các phần tử có giá trị âm trong A
def positiveA():
    while True:
        try:
            n=int(input('n='))
            if n>0:
                break
            else:
                print('Enter positive number.')
        except ValueError:
            print('Enter positive number.')

    A=[]
    for i in range(n):
        while True:
            try:
                num=int(input(f'Enter the {i+1}-th number: '))
                A.append(num)
                break
            except ValueError:
                print('Enter interact number.')
    #Delete negative number in A
    k=0
    while k<len(A):
        if A[k]<0:
            A.remove(A[k])
        else: 
            k+=1
    print(*A)

positiveA()
