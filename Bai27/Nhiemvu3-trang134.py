#Thiết hàm merge-str(s1,s2) với s1 s2 là hai xâu cần gộp
#Yêu cầu: lấy lần lượt từng kí tự của s1, s2 đưa vào xâu kết quả. Nếu có một xâu hết kí tự thì đưa phần còn lại của xâu dài hơn vào xâu kết quả.
#VD: s1='1111', s2='0000', c=1 thì xâu kết quả là '10101010'


'''def merge_str(s1,s2):
    s=''
    l1=len(s1)
    l2=len(s2)
    l=min(l1,l2)
    for i in range(l):
        s=s+s1[i]+s2[i]
    if l1<l2:
        for i in range(l,l2):
            s=s+s2[i]
    if l2<l1:
        for i in range(l,l1):
            s=s+s1[i]
    return s

print(merge_str('111','000'))'''



'''def merge_str(s1, s2):
    result = ''
    len1, len2 = len(s1), len(s2)
    min_len = min(len1, len2)

    # Lấy lần lượt từng ký tự từ s1 và s2
    for i in range(min_len):
        result += s1[i] + s2[i]

    # Thêm phần còn lại của xâu dài hơn
    result += s1[min_len:] + s2[min_len:]

    return result

# Ví dụ
s1 = '1111'
s2 = '0000'
print(merge_str(s1, s2))  # Kết quả: '10101010'''




while True:
    s1=input('Input s1: ').strip()
    if s1=='':
        print('Chưa nhập xâu s1.')
        continue
    break
while True:
    s2=input('Input s2: ').strip()
    if s2=='':
        print('Chưa nhập xâu s2.')
        continue
    break

def merge_str(s1,s2):
    result=''
    len1,len2=len(s1),len(s2)
    min_len=min(len(s1),len(s2))
    for i in range(min_len):
        result+=s1[i]+s2[i]
    if len1<len2:
        for i in range(min_len,len2):
            result+=s2[i]
    else:
        for i in range(min_len,len1):
            result+=s1[i]
    return result
print(merge_str(s1,s2))
