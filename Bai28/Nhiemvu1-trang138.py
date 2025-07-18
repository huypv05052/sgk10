#Viết hàm với đầu vào là ds A chứa số và số thực x. Trả về ds B từ A gồm các số >= x



#Xây dựng hàm
def select(A,x):
    B=[]
    for i in range(len(A)):
        if A[i]>=x:
            B.append(A[i])
    return f'Các số trong A và >= {x}: {B}'


#nhập n hợp lệ
while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập n nguyên dương.')

    except ValueError:
        print('Nhập n nguyên dương.')


#nhập n giá trị cho A
A=[]
for i in range(n):
    while True:
        try:
            num=int(input(f'Nhập phần tử thứ {i+1}: '))
            A.append(num)
            break
        except ValueError:
            print('Chỉ được nhập số.')

#nhập x
while True:
    try:
        x=float(input('Nhập giá trị cho x: '))
        break
    except ValueError:
        print('Chưa hợp lệ.')


print(select(A,x))
