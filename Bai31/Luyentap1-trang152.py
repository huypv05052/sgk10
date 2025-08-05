#Viết CT nhập số thực dương a. Kiểm tra dữ liệu:
#Nếu a<= 0 thì thông báo nhập lại. Chương trình dừng sau khi nhập đúng


def main():
    while True:
        try:
            a=float(input('a='))
            if a>0:
                break
            else:
                print('Nhập số thực dương khác không.')
        except ValueError:
            print('Nhập số thực dương khác không.')
    return f'Bạn đã nhập: {a}'

print(main())
