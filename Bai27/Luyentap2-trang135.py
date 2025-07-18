#Viết CT nhập 2 số tự nhiên từ bàn phím, hai số cách nhau bằng dấu cách. Tính và in ra tổng của 2 số


def tong2so():
    while True:
        nums=input('Nhập 2 số tự nhiên cách nhau bằng dấu cách: ').split()
        if len(nums)!=2:
            print('Chưa hợp lệ.')
            continue
        try:
            a,b=int(nums[0]),int(nums[1])
            if a<0 or b<0:
                print('không hợp lệ.')
                continue
            print(f'{a}+{b}={a+b}')
            break
        except ValueError:
            print('Dữ liệu vào không hợp lệ.')

tong2so()
