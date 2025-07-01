#Viết chương trình Python in ra màn hình bảng nhân trong phạm vi 10
# Method 1
for i in range(1, 11):
    for j in range(1, 11):
        print(str(j)+'x'+str(i)+'='+str(j*i), end='\t')
    print()


# Method 2: use f-string
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{j}x{i:1}={j*i:2}', end='\t')
    print()
