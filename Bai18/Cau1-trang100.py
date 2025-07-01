#Viết chương trình nhập 3 số thực dương a, b, c và tính chu vi, diện tích tam giác có độ dài ba cạnh là a, b, c
# suggest: S = sqrt(p(p-a)(p-b)(p-c)) , p là nửa chu vi
# Method 1
import math
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

p = (a + b + c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'Chu vi tam giác bằng: {a+b+c}')
print(f'Diện tích tam giác bằng: {s}')
