#Viết lệnh xóa phần tử cuối của danh sách, thêm phần tử vào đầu danh sách
while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập số nguyên dương.')
    except ValueError:
        print('Nhập số nguyên dương.')
A=[]
for i in range(n):
    element=input(f'Nhập phần tử A[{i+1}]: ')
    A.append(element)
A.pop()
A.insert(0, input('Nhập giá trị A[0]: '))
print(*A)
