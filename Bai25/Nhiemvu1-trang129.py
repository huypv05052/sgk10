#Viết hàm yêu cầu người dùng nhập họ tên rồi đưa lời chào ra màn hình.


def chuanHoaTen(name):
    return ' '.join(k.capitalize() for k in name.split())

def greet():
    while True:
        name=input('Nhập họ tên của bạn: ').strip()
        if name=='':
            print('Chưa nhập họ tên.')
            continue
        elif any(k.isdigit() for k in name):
            print('Không nhập số.')
            continue
        break
    name=chuanHoaTen(name)
    return f'Chào bạn {name}'

print(greet())
