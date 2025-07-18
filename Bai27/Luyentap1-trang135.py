#Thiết lập hàm power(a,b,c) với a,b,c là số nguyên. Hàm trả về (a+b)^c

'''def power(a,b,c):
    return pow(a+b,c)

print(power(1,2,3))
print(power(2,-3,0.5))'''

def power(a,b,c):
    return pow(a+b,c)


while True:
    try:
        a=int(input('a='))
        b=int(input('b='))
        c=int(input('c='))
        print(f'Kết quả: {power(a,b,c)}')
        break
    except ValueError:
        print('Nhập số nguyên.')
