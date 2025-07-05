#Nhập số n từ bàn phím, nhập danh n tên học sinh, in ra danh sách học sinh, mỗi tên trên một dòng. In ra danh sách ngược với danh sách đã nhập


def dsName():
    while True:
        try:
            n=int(input('n='))
            if n>0:
                break
            else:
                print('Nhập số nguyên dương')
        except ValueError:
            print('Nhập số nguyên dương.')
    
    dsTen=[]
    for i in range(n):
        while True:
            tenhs=input(f'Nhập tên học sinh thứ {i+1}: ')
            if tenhs=='':
                print('Không được để trống.')
            elif tenhs[0]==' ':
                print('Ký tự đầu không được cách.')
            elif any(char.isdigit() for char in tenhs):
                print('Không được chứa số.')
            else:
                dsTen.append(tenhs)
                break
    
    # for i in range(len(dsTen)):
    #     print(f'{i+1}. {dsTen[i]}')
    

    print('Danh sách đảo ngược thứ tự đã nhập vào:')
    stt=1
    for ten in reversed(dsTen):
        print(f'{stt}. {ten}')
        stt+=1


    #Dùng enumerate
    for i, ten in enumerate(reversed(dsTen), 1):   #start=1, chỉ số bắt đầu từ 1
        print(f'{i}. {ten}')
dsName()
