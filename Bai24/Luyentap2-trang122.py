#Viết chương trình kiểm tra xâu s có chứa số hay không.
'''def checkNumberS():
    while True:
        s=input('Nhập xâu s: ')
        if len(s)>0:
            break
        else:
            print('Xâu s không được rỗng.')
    
    if any(k.isdigit() for k in s):
        print('Xâu s có chứa số.')
    else:
        print('Xâu s không chứa số.')

checkNumberS()'''



# Lấy vị trí chứa số trong xâu
def checkNumberS():
    while True:
        s=input('Nhập xâu s: ')
        if len(s)>0:
            break
        else:
            print('Xâu s không được rỗng.')
    
    vi_tri=[]
    for i,k in enumerate(s):
        if k.isdigit():
            vi_tri.append(i)
    if len(vi_tri)>0:
        print(f'Xâu s có số ở vị trí: {vi_tri}')
    else:
        print('Xâu s không có số.')

checkNumberS()
