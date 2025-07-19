#Viết hàm yêu cầu như sau:
#- Đầu vào là ds sList, các phần tử là xâu kí tự
#- Đầu ra là ds cList, phần tử là kí tự đầu tiên của các xâu kí tự tương ứng trong ds sList

def getFirstLetter():
    while True:
        sList=input('Nhập các từ cách nhau bởi dấu cách: ').split()
        if not sList:
            print('Chưa hợp lệ.')
            continue
        break
    cList=[i[0] for i in sList if i]        #Đảm bảo từ không rỗng
    return f'Kí tự đầu tiên của các xâu trong sList: {cList}'

A=getFirstLetter()
print(A)
