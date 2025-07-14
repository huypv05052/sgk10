#Viết chương trình yêu cầu nhập từ bàn phím một xâu, sau đó thông báo:
#-Tổng số các kí tự là chữ số của xâu       (isdigit)
#-Tổng số các kí tự là chữ cái tiếng Anh trong xâu (isalpha)
# Viết hàm cho mỗi yêu cầu


while True:
    s=input('Nhập xâu kí tự s: ').strip()
    if s=='':
        print('Chưa nhập xâu s.')
        continue        #Quay lại vòng lặp, yêu cầu nhập lại
    break           #Nếu s khác rỗng, thoát khỏi vòng lặp


#Hàm đếm số trong xâu s
def countNumber(s):
    count=0
    for i in range(len(s)):         #for i in s:
        if s[i].isdigit():          #if i.isdigit():
            count+=1
    return f'Có {count} chữ số trong xâu s.'
print(countNumber(s))

#hàm đếm chữ cái tiếng Anh trong xâu s
def countLetter(s):
    count=0
    for i in s:
        if i.isalpha():         #isalpha đếm luôn dấu
            count+=1
    return f'Có {count} chữ cái trong xâu s.'
print(countLetter(s))


import string
def countEnglishLetter(s):
    count=0
    for i in s:
        if i in string.ascii_letters:   #a-z và A-Z
            count+=1
    return f'Có {count} chữ cái tiếng Anh trong xâu s.'
print(countEnglishLetter(s))


#Method2: Dùng biểu thức chính quy (regular expression)
import re
def count_english_letters(s):
    letters=re.findall(r'[A-Za-z]', s)
    return f'Có {len(letters)} chữ cái tiếng Anh trong xâu s.'
print(count_english_letters(s))
