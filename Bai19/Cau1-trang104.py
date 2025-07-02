#Giá bán cam tại siêu thị như sau
#Nếu mua dưới 5kg: 12k/kg
#nếu mua lớn hơn 5kg: 10k/kg
#Viết chương trình nhập số lượng mua, sau đó tính số tiền phải trả


def tinhTien():
    while True:
        try:
            k = float(input('Nhập số kg đã mua: '))
            if k <= 0:
                print('Số kg không hợp lệ! Vui lòng nhập lại!')
                continue
            break
        except ValueError:
            print('Lỗi! Số kg nhập vào không hợp lệ!')
    if k <= 5:
        tien = k*12
    else:
        tien = k*10
    return f'Số tiền cần trả là: {tien} nghìn đồng'
print(tinhTien())
