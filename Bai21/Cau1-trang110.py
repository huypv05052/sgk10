#Cho cấp số cộng u1 = 1, d = 3. Viết chương trình in ra số lớn nhất của CSC và nhỏ hơn 100


u1, d = 1, 3
un=u1
while un < 100:
    result = un
    un += d
print(f'Giá trị lớn nhất và nhỏ hơn 100 của csc là: {result}')




#Nâng cấp: tìm giá trị max của csc nhỏ hơn m bất kỳ, và tìm số hàng thứ mấy
def maxCsc(m):
    u1, d = 1, 3
    un=u1
    while un < m:
        result = un
        un += d
    return f'Giá trị lớn nhất trong dãy và nhỏ hơn {m} là: {result} và nó là số hạng thứ {((result-u1)/3)+1:.0f}'

print(maxCsc(100))
print(maxCsc(200))
print(maxCsc(500000))
