#Viết CT nhập các số nguyên m,n cách nhau bởi dấu cách, đưa ra tổng, hiệu, tích, thương của nó

def main():
    while True:
        try:
            values=input('Nhập 2 số cách nhau bởi dấu cách: ').split()
            if len(values)!=2:
                print('Chưa hợp lệ.')
                continue
            m,n=map(int,values)
            break
        except ValueError:
            print('Chưa hợp lệ.')
    
    print(f'{m}+{n}={m+n}')
    print(f'{m}-{n}={m-n}')
    print(f'{m}*{n}={m*n}')
    print(f'{m}/{n}={round(m/n,2) if n!=0 else "Không chia được cho 0"}')

main()
