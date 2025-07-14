#Thiết lập hàm f_sum(A,b) dùng để tính tổng các số của ds A theo quy định:
#Nếu b=0 thì tính tổng các số của ds A
#Nếu b!=0 thì chỉ tính tổng các số dương của A
#Note: Chương trình luôn check giá trị của đối số b trước khi tính tổng các số trong A


#Method 1:
'''def f_sum(A,b):
    s=0
    for i in A:
        if b==0:
            s+=i
        else:
            if i>0:
                s+=i
    return s'''



#Method2: use comprehension (cú pháp ngắn gọn)
def f_sum(A,b):
    if b==0:
        return f'Tổng các số trong list A: {sum(A)}'
    else:
        return f'Tổng các số dương trong list A: {sum(i for i in A if i>0)}'



'''while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập n nguyên dương.')
    except ValueError:
        print('Nhập n nguyên dương.')

A=[]
for i in range(n):
    while True:
        try:
            num=int(input(f'A[{i+1}]='))
            A.append(num)
            break
        except ValueError:
            print('Nhập số nguyên.')
print(f'Các số trong list A: {A}')'''

# print(f_sum(A,0))
# print(f_sum(A,10))




#Nhập giá trị cho A trên một dòng, các số cách nhau bỏi dấu cách:

while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập n nguyên dương.')
    except ValueError:
        print('Nhập n nguyên dương.')

'''A=list(map(int, input(f'Nhập {n} số nguyên tách ra bằng dấu cách: ').split()))
if len(A)!=n:
    print('Nhập sai số lượng phần tử.')
else:
    print(f'List A: {A}')'''

#Nhập số cho A:
while True:
    try:
        num=input(f'Nhập {n} số cách nhau bằng dấu cách: ').split()
        if len(num)!=n:
            print(f'Phải nhập đúng {n} số. Đã nhập {len(num)}')
            continue
        A=list(map(int,num))
        break
    except ValueError:
        print('Chỉ được nhập số nguyên.')
print(f'List A: {A}')
print(f_sum(A,2))
print(f_sum(A,0))
