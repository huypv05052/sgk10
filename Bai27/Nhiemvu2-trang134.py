#Thiết lập hàm f_dem(msg, sep) dùng để đếm số các từ của xâu msg với ký tự tách là sep
#EX: f_dem('Python programming 12', ' ') -> 3
#EX: f_dem('Python programming 12', '-') -> 1
#Để tách xâu msg thành các từ, dùng lệnh split(), tham số sep chính là tham số của split()


while True:
    s=input('Nhập xâu s: ').strip()
    if s=='':
        print('Chưa nhập xâu s.')
        continue
    break
# print(s)

'''def f_dem(s,i):
    lst_s=s.split(i)                #Không tối ưu nếu xâu có nhiều dấu cách
    return f'Xâu s có {len(lst_s)} từ.'
print(f_dem(s,' '))'''

def f_dem(s):
    lst_s=s.split()
    return f'Xâu s có {len(lst_s)} từ'

print(f_dem(s))
