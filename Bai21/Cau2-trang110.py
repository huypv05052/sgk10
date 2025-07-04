#Viết chương trình đếm trong 100 số tự nhiên đầu tiên có bao nhiêu số thỏa điều kiện: chia hết 5 hoặc chia cho 3 dư 1

count = 0
i = 0
while i <= 100:
    if (i % 5 == 0) or (i%3==1):
        count+=1
    i += 1
print(count)
