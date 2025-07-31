#Viết CtT nhập số tự nhiên n và nhập n số nguyên đưa vào ds A. In ds A ra màn hình



# while True:
#     try:
#         n=int(input('n='))
#         if n>0:
#             break
#         else:
#             print('Nhập số tự nhiên.')
#     except ValueError:
#         print('Nhập số tự nhiên.')
    
# A=[]
# for i in range(n):
#     while True:
#         try:
#             number=int(input(f'Nhập giá trị cho phần tử A[{i}]: '))
#             A.append(number)
#             break
#         except ValueError:
#             print('Chưa hợp lệ.')

# print(f'Danh sách A: {A}')


def main():
    while True:
        try:
            n=int(input('n='))
            if n>0:
                break
            else:
                print('Nhập số tự nhiên lớn hơn 0.')
        except ValueError:
            print('Nhập số tự nhiên lớn hơn 0.')
    
    #Nhập số cho danh sách
    A=[]
    for i in range(n):
        while True:
            try:
                number=int(input(f'Nhập giá trị cho phần tử A[{i}]: '))
                A.append(number)
                break
            except ValueError:
                print('Chỉ nhập số nguyên.')
    

    print(f'Danh sách A: {A}')


main()
