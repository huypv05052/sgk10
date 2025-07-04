#Viết chương trình in dãy chữ cái tiếng Anh từ A tới Z theo 3 hàng ngang, 2 hàng đầu có 10 chữ cái, hàng thứ 3 có 6 chữ cuối


# Method 1: use while
i = 0
k = 65 #bắt đầu từ số thứ tự của chữ A (65-->90)
while k < 91:
    i+=1
    if i%10 == 0:
        print(chr(k))   # khôn có end => tự động xuống dòng
    else:
        print(chr(k), end=' ')   # Có end=' ', in cùng dòng, tách ra bằng dấu cách
    k += 1



# Method 2: use for
k = 65
for i in range(26):
    print(chr(65+i), end=' ')
    if i==9 or i==19:
        print()


#use function:
def alphaPrint():
    i = 0
    k = 65
    while k < 91:
        i += 1
        if i%10==0:
            print(chr(k))
        else:
            print(chr(k), end=' ')
        k+=1
alphaPrint()
