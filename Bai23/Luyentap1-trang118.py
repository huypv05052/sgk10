#Cho dãy [1, 2, 2, 3, 4, 5, 5]. Viết lệnh thưc hiện:
#a) Chèn số 1 vào ngay sau giá trị 1 của dãy
#b) Chèn số 3 và 4 vào danh sách để dãy số có 3 và 4 liền nhau hai lần

lst=[1, 2, 2, 3, 4, 5, 5, 3, 4]
#a)
index_1=lst.index(1)    #Tìm chỉ số của số 1
lst.insert(index_1+1, 1)        #Sau số 1, chèn số 1
print(lst)


#b) 

# for i in range(len(lst)-1):
#     if lst[i]==3 and lst[i+1]==4:
#         vi_tri_chen = i+2
#         break
lst=[1, 2, 2, 3, 4, 5, 5, 3, 4, 1, 3, 4]
vi_tri_chen=[]
i=0
while i<len(lst)-1:
    if lst[i]==3 and lst[i+1]==4:
        vi_tri_chen.append(i+2)
        i+=2
    else:
        i+=1
print(vi_tri_chen)

for vt in reversed(vi_tri_chen):
    lst.insert(vt, 3)
    lst.insert(vt+1, 4)

print(lst)
