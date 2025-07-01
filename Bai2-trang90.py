#Viết chương trình Python in ra màn hình bảng nhân trong phạm vi 10
for i in range(1, 11):
    for j in range(1, 11):
        print(str(j)+'x'+str(i)+'='+str(j*i), end='\t')
    print()
