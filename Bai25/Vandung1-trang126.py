#Viết CT nhập 2 số tự nhiên, cách nhau bởi dấu cách. Đưa ra ước chung lớn nhất của 2 số

def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a

while True:
    num_str=input('Nhập 2 số tự nhiên phân biệt bằng dấu cách: ').strip()
    if num_str=='':
        print('Chưa hợp lệ. Nhập lại.')
        continue
    lst_num=num_str.split()
    if len(lst_num)!=2:
        print('Không hợp lệ.')
        continue

    try:
        a=int(lst_num[0])
        b=int(lst_num[1])
        if a<=0 or b<=0:
            print('Chưa hợp lệ. Nhập lại.')
            continue
        break
    except ValueError:
        print('Dữ liệu vào chưa hợp lệ. Nhập lại.')

result=ucln(a,b)
print(f'UCLN({a},{b})={result}')
