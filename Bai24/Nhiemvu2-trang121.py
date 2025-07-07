#Nhập một xâu S từ bàn phím, kiểm tra xem xâu S có chứa xâu con "10" hay không

#Method 1
'''s=input('Nhập xâu S: ')
s1="10"
if s1 in s:
    print(f'{s1} nằm trong xâu {s}')
else:
    print(f'{s1} không nằm trong xâu {s}')'''


#Method 2:
'''s=input('Nhập xâu s: ')
result=False
for i in range(len(s)-1):
    if s[i]=='1' and s[i+1]=='0':
        result=True
        break
if result==True:
    print(f'Xâu s chứa xâu "10"')
else:
    print(f'Xâu s không chứa xâu "10"')'''


#Lấy vị trí của xâu 10 trong xâu s nếu có:
s=input('Nhập xâu s: ')
vi_tri=[]
i=0
while i<len(s)-1:
    if s[i]=='1' and s[i+1]=='0':
        vi_tri.append(i)
        i+=2
    i+=1
print(f'Vị trí chứa xâu "10" trong s: {vi_tri}')
