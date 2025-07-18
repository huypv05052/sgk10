#Viết CT nhập 2 số tự nhiên từ bàn phím, cách nhau bằng dấu phẩy, in ra ước chung lớn nhất của 2 số



def ucln(m,n):
    while n!=0:
        m,n=n,m%n
    return m

def main():
    while True:
        nums=input('Nhập 2 số tự nhiên cách nhau bằng dấu phẩy: ').split(',')
        if len(nums)!=2:
            print('Chưa hợp lệ.')
            continue

        a,b=int(nums[0]),int(nums[1])
        if a<=0 or b<=0:
            print('Không hợp lệ.')
            continue
        
        print(f'UCLN({a},{b})={ucln(a,b)}')
        break

main()
