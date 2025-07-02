#Viết chương trình tính tổng: S = 1 + 1/2 + 1/3 + ... + 1/n
def tinhTong():
    while True:
        try:
            n = int(input('n = '))
            if n <= 0:
                print('Nhập số nguyên dương.')
                continue
            break
        except ValueError:
            print('Nhập số nguyên dương!')
    
    S = 0
    for i in range(1, n+1):
        S += 1/i
    return f'Tổng S = {S:.2f}'

print(tinhTong())
