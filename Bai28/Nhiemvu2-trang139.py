#Viết hàm đầu vào là xâu str và số c, trả về list B các từ được tách ra từ xâu str nhưng được chuyển đổi tùy thuộc vào c như sau:
#c==0: B chứa các từ in hoa
#c==1: B chứa các từ in thường
#c==2: B chứa các từ in hoa chữ cái đầu



#build hàm, dùng comprehensions
def tach_tu(str,c):
    A=str.strip().split()
    if c==0:
        B=[k.upper() for k in A]
    elif c==1:
        B=[k.lower() for k in A]
    elif c==2:
        B=[k.title() for k in A]
    return B

# A=['viet', 'huy']
# print(tach_tu(A,0))
# print(tach_tu(A,1))
# print(tach_tu(A,2))
# print(tach_tu(A,3))

while True:
    A=input('Nhập các từ cách nhau bằng dấu cách: ').strip()
    if A=='':
        print('Chưa nhập gì.')
        continue
    break


while True:
    try:
        c=int(input('Nhập c (0 in hoa, 1 in thường, 2 in hoa chữ đầu): '))
        if c in (0,1,2):
            break

        print('Nhập c chưa hợp lệ.')
    except ValueError:
        print('Nhập c chưa hợp lệ.')


print(tach_tu(A,c))
