#Viết hàm tachDayA(), đầu vào là ds A, đầu ra là ds B,C:
#-Ds B chứa các phần tử có chỉ số chẵn từ A
#-Ds C chứa các phần tử có chỉ số lẻ từ A


def tachDayA():
    while True:
        s=input('Nhập nhiều xâu cách nhau bằng dấu cách: ').split()
        if not s:
            print('Chưa hợp lệ.')
            continue
        break
    B=[]
    for i,value in enumerate(s):
        if i%2==0:
            B.append(value)

    C=[value for i,value in enumerate(s) if i%2==1]
    return B,C

B,C=tachDayA()
print(f'Danh sách B (chỉ số chẵn): {B}')
print(f'Danh sách C (chỉ số lẻ): {C}')
