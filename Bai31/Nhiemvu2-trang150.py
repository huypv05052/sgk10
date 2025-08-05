#Viết CT nhập 3 số thực a,b,c và tìm nghiệm của pt bậc hai:ax2+bx+c=0
#a=b=c=0: PT có vô số nghiệm
#a=b=0, c!=0: PT vô nghiệm
#a=0, b!=0: PT có nghiệm duy nhất (PT bậc nhất bx+c=0)
#a!=0: delta=b2-4ac


def input_data():
    while True:
        numbers=input('Nhập 3 hệ số cách nhau bởi dấu cách: ').split()
        if len(numbers)!=3:
            print('Chưa hợp lệ.')
            continue

        try:
            a,b,c=float(numbers[0]),float(numbers[1]),float(numbers[2])
            return a, b, c
        except ValueError:
            print('Chưa hợp lệ.')


def sqrt(x):
    return x**0.5


def main(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                print('PT có vô số nghiệm.')
            else:
                print('PT vô nghiệm.')
        else:
            x=-c/b
            if x==-0.0:
                x=0.0                
            print(f'PT có nghiệm duy nhất x = {x}')
    else:
        delta = b*b - 4*a*c
        if delta<0:
            print('PT vô nghiệm.')
        elif delta==0:
            x=-b/(2*a)
            print(f'PT có nghiệm kép x1 = x2 = {x}')
        else:
            x1=(-b-sqrt(delta))/(2*a)
            x2=(-b+sqrt(delta))/(2*a)
            print(f'PT có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}')

a,b,c=input_data()
main(a,b,c)
