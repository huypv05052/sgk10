#Giả sử giá điện được tính như sau
#Với mức tiêu thụ từ 0-50kWh: giá 1.678k/kWh
#Với mức tiêu thụ từ 51-100: giá 1.734k/kWh
#Với mức trên 101kWh: giá 2.014k/kWh
#Viết chương trình nhập số điện tiêu thụ trong tháng của gia đình và tính số tiền điện phải trả



# Method 1
k = float(input('Nhập số kWh điện tiêu thụ của tháng: '))
if k < 51:
    t = k*1.678
elif (k >= 51 and k < 101):
    t = k*1.734
else:
    t = k*2.014
print(f'Số tiền phải trả là: {t:.2f} nghìn đồng')



# Method 2
def tienDien():
    while True:
        try:
            k = float(input('Nhập số kWh điện tiêu thụ: '))
            if k <= 0:
                print('Số kWh không hợp lệ. Vui lòng nhập lại!')
                continue
            break
        except ValueError:
            print('Số kWh không hợp lệ. Vui lòng nhập lại!')
    if k <= 50:
        return f'Số tiền phải trả: {k*1.678} nghìn đồng'
    elif (k>50 and k<=100):
        return f'Số tiền phải trả: {k*1.678 + (k-50)*1.734:.2f} nghìn đồng'
    else:
        return f'Số tiền phải trả: {50*1.678 + 50*1.734 + (k-100)*2.014:.2f} nghìn đồng'
    
print(tienDien())
