#Thuật toán sắp xếp
#Bubble sort



while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Chưa hợp lệ.')
    except ValueError:
        print('Chưa hợp lệ.')

A=[]
for i in range(n):
    while True:
        try:
            number=int(input(f'Nhập giá trị cho phần tử A[{i}]: '))
            A.append(number)
            break
        except ValueError:
            print('Nhập số nguyên.')
print(f'Đã nhập danh sách A: {A}')

#sắp xếp A

def bubble_sort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j]>A[j+1]:            #Giảm thì A[j]<A[j+1]
                A[j],A[j+1]=A[j+1],A[j]

bubble_sort(A)
print(f'Danh sách A sau khi sắp xếp: {A}')
