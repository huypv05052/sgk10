#Nhập một dãy n số bất kỳ. Tính tổng, trung bình của dãy và in ra thành hàng ngang


#Method 1: Bình thường
n=int(input('n='))
A=[]
for i in range(n):
    number=int(input(f'Nhập số thứ {i+1}: '))
    A.append(number)

print('Dãy số đã nhập: ')
for i in range(n):
    print(A[i], end=' ')
print()
print(f'Tổng các số trong dãy: {sum(A)}')
print(f'Trung bình các số trong dãy: {sum(A)/n:.1f}')



#Method 2: Kiểm soát dữ liệu vào là số nguyên (có thể âm hoặc dương)
while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Số phần tử phải là số nguyên dương.')
    except ValueError:
        print('Số phần tử phải là số nguyên dương.')

#Nhập giá trị cho A:
A = []
for i in range(n):
    while True:
        try:
            number=int(input(f'Nhập giá trị cho phần tử A[{i+1}]: '))
            if number<0:
                print('Phải nhập giá trị là số nguyên dương.')
            else:
                A.append(number)
                break
        except ValueError:
            print('Phải nhập giá trị là số nguyên dương.')
print('Dãy số đã nhập: ')
print(*A)       #In ra danh sách A (thay vi dùng vòng lặp)
print(f'Tổng các giá trị trong danh sách bằng: {sum(A)}')
print(f'Trung bình các giá trị trong danh sách bằng: {sum(A)/n:.1f}')



#Method 3: dùng hàm
def dsA():
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
        while True:
            try:
                number=int(input(f'Nhập giá trị cho phần tử A[{i+1}]: '))
                if number<0:
                    print('Nhập số nguyên dương.')
                else:
                    A.append(number)
                    break
            except ValueError:
                print('Nhập số nguyên dương.')

    print('Giá trị đã nhập cho danh sách: ')
    print(*A)

dsA()     
