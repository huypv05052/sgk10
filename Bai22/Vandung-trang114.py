#Nhập dãy số A. viết chương trình tìm giá trị và chỉ số của phần tử lớn nhất và nhỏ nhất của A.
def maxMinA():
    while True:
        try:
            n=int(input('n='))
            if n>0:
                break
            else:
                print('Nhập số nguyên dương.')
        except ValueError:
            print('Nhập số nguyên dương.')
    A=[]
    for i in range(n):
        while True:
            try:
                number=int(input(f'Nhập giá trị phần tử A[{i+1}]: '))
                A.append(number)
                break
            except ValueError:
                print('Nhập giá trị là một số nguyên.')
    print(*A)
    maxValue=max(A)
    maxIndex=A.index(maxValue)
    minValue=min(A)
    minIndex=A.index(minValue)
    print(f'Phần tử lớn nhất là A[{maxIndex}]: {maxValue}')
    print(f'Phần tử nhỏ nhất là A[{minIndex}]: {minValue}')
maxMinA()
