#Cho xâu s. Viết lệnh trích ra 3 ký tự đầu tiên (xâu con) của s
def first3CharacterS():
    while True:
        s=input('Nhập xâu s: ')
        if len(s)>=3:
            result=[]
            for i in range(3):
                result.append(s[i])
            print(f'3 ký tự đầu tiên của s là: {result}')
            # print(f'3 ký tự đầu tiên của s là: {list(s[:3])}')
            break
        else:
            print('Xâu s ít hơn 3 kí tự, nhập lại.')

first3CharacterS()
