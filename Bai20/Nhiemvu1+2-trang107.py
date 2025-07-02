#Nhiệm vụ 1 và 2: Nhập số tự nhiên n từ bàn phím và in ra và đếm dãy các ước của n theo chiều ngang màn hình
def demUoc():
    while True:
        try:
            n = int(input('n = '))
            if n <= 0:
                print('Vui lòng nhập số nguyên dương!')
                continue
            break
        except ValueError:
            print('Vui lòng nhập số nguyên dương!')
    
    result = f'Các ước số của {n} là: '
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += f'{i} '
            count += 1
    result += f'\nTổng cộng có {count} ước của {n}'
    return result

print(demUoc())
