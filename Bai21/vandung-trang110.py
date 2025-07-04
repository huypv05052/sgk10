#Viết chương trình in các số tự nhiên 1 tới 100, in thành 10 hàng, mỗi hàng 10 số
#while loop:
i = 1
while i <= 100:
    if i%10==0:
        print(i)
    else:
        print(i, end='\t')
    i+=1


#for loop:
for i in range(1, 101):
    print(i, end=' ')
    if i%10==0:
        print()
