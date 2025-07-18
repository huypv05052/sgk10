#Thiết lập hàm change(ho_ten,c). Trả về xâu ho_ten in hoa nếu c==0, ngược lại trả về ho_ten in thường


def change(ho_ten,c):
    if c==0:
        result=ho_ten.upper()
    else:
        result=ho_ten.lower()
    return result



while True:
    ho_ten=input('Nhập họ tên: ').strip()
    if ho_ten=='':
        print('Chưa nhập gì')
        continue

    elif any(k.isdigit() for k in ho_ten):
        print('Không được chứa số.')
        continue

    break


# print('In hoa: ',change(ho_ten,0))
# print('In thường: ',change(ho_ten,1))

while True:
    try:
        c=int(input('Nhập 0 để in hoa, nhập số bất kì để in thường: '))
        print(change(ho_ten,c))
        break
    except ValueError:
        print('Nhập c cho hợp lệ.')
