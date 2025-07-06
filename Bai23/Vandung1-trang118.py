#Viết CT nhập n từ bàn phím, tạo và in ra màn hình dãy số A gồm n số tự nhiên chẵn đầu tiên

def evenA():
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
        A.append(2*i)
    print(f'Dãy A gồm {n} số chẵn đầu tiên: {A}')

evenA()
