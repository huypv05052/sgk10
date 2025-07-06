#Cho dãy số A. Viết chương trình tìm chỉ ra vị trí đầu tiên của dãy A mà 3 số hạng liên tiếp có giá trị 1, 2, 3. Nếu tìm thấy thì thông báo vị trí tìm thấy, ngược lại thông báo "Không tìm thấy mẫu"

A=[3, 4, 5, 7, 8, 4, 3, 8, 1, 2, 3, 4, 5, 6, 0, -1, 2, 3]
p=[1, 2, 3]         #mẫu cần tìm
pkq=-1              #Vị trí khởi đầu: chưa thấy =-1
i=0
while i<=len(A)-3 and pkq==-1:
    if A[i]==p[0] and A[i+1]==p[1] and A[i+2]==p[2]:
        pkq=i
    i+=1

if pkq>=0:
    print(f'Tìm thấy mẫu {p} tại vị trí {pkq}')
else:
    print(f'Không tìm thấy mẫu {p}')


#Use function:
def timMau(p, A):
    for i in range(len(A)-len(p)+1):
        found=True
        for j in range(len(p)):
            if A[i+j] != p[j]:
                found=False
                break
        if found:
            return i
    return -1

print(timMau(p, A))

k=[7, 8]
B=[4, 5, 6, 7, 8, 9]
print(timMau(k, B))
