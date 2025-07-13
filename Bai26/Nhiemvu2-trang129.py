#Viết hàm prime(n) với tham số là số tự nhiên n và trả về True nếu n là số nguyên tố, trả về False nếu n không phải số nguyên tố.


'''def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==1:
        return True
    else:
        return False
    
print(prime(10))'''

def prime(n):
    if n<0:
        print(f'Giá trị vào không hợp lệ.')
        return False
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1): #Chạy tới văn bậc hai là đủ
        if n%i==0:
            return False
    return True

print(prime(2))
print(prime(-2))
