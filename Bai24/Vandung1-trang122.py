#Cho 2 xâu s1, s2. Viết chương trình chèn xâu s1 vào giữa xâu s2, tại vị trí len(s2)//2. In kết quả ra màn hình

def insertString():
    while True:
        s1=input('s1 = ')
        if len(s1)>=0:
            break
        else:
            print('Chưa nhập xâu s1.')
    
    while True:
        s2=input('s2 = ')
        if len(s2)>=2:
            break
        else:
            print('Xâu s2 phải có ít nhất 2 kí tự.')
        
    print(f'Xâu s1: {s1}')
    print(f'Xâu s2: {s2}')
    #chèn s2 vào giữa s1:
    '''mid=len(s2)//2
    result=''
    for i in range(len(s2)):
        if i==mid:
            result+=s1
        result+=s2[i]
    print(f'Kết quả sau khi chèn s1 vào giữa s2: {result}')'''

    #cách 2: dùng lát cắt (slicing)
    mid=len(s2)//2
    result = s2[:mid] + s1 + s2[mid:]
    print(f'Kết quả sau khi chèn s1 vào giữa s2: {result}')
insertString()
