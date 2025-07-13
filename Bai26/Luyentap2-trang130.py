#Viết hàm numbers(s) đếm số các chữ số có trong xâu s
#Ví dụ: numbers('0101acb')=4

def numbers():
    while True:
        s=input('Nhập xâu s: ').strip()
        if s=='':
            print('Chưa nhập xâu s.')
            continue
        break
    count=0
    for i in range(len(s)):
        if s[i].isdigit():
            count+=1
    return f'Có {count} số trong xâu s.'

print(numbers())




#Đúng theo yêu cầu thì như dầy:
'''def input_string():
    while True:
        s = input('Nhập xâu s: ').strip()
        if s == '':
            print('Chưa nhập xâu s.')
            continue
        return s

def numbers(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    return count

# Gọi hàm:
s = input_string()
print('Số chữ số trong xâu là:', numbers(s))'''
