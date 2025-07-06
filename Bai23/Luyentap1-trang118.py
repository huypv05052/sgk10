#Cho dãy [1, 2, 2, 3, 4, 5, 5]. Viết lệnh thưc hiện:
#a) Chèn số 2 vào ngay sau các giá trị 1 của dãy
#b) Chèn số 3 và 4 vào danh sách để dãy số có 3 và 4 liền nhau hai lần

#a)
# index_1=lst.index(1)    #Tìm chỉ số của số 1
# lst.insert(index_1+1, 1)        #Sau số 1, chèn số 1
# print(lst)
lst=[1, 5, 3, 4, 5, 1, 5, 3, 1, 4]
vi_tri_chen_2=[]
i=0
while i<len(lst)-1:
    if lst[i]==1:
        vi_tri_chen_2.append(i+1)
        i+=2
    i+=1
print(f'Vị trí cần chèn 2: {vi_tri_chen_2}')
for k in reversed(vi_tri_chen_2):
    lst.insert(k, 2)
print(f'Danh sách sau khi chèn 2: {lst}')





#b) 

# for i in range(len(lst)-1):
#     if lst[i]==3 and lst[i+1]==4:
#         vi_tri_chen = i+2
#         break
lst=[1, 2, 2, 3, 4, 5, 5, 3, 4, 1, 3, 4]
vi_tri_chen_34=[]
i=0
while i<len(lst)-1:
    if lst[i]==3 and lst[i+1]==4:
        vi_tri_chen_34.append(i+2)
        i+=2
    i+=1
print(f'Vị trí cần chèn 3, 4: {vi_tri_chen_34}')
#chèn 3, 4
for k in reversed(vi_tri_chen_34):
    lst.insert(k, 3)
    lst.insert(k+1, 4)
print(f'Danh sách sau khi chèn 3, 4: {lst}')
