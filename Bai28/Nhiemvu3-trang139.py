#Viết CT yêu cầu thực hiện lần lượt các việc sau, mỗi việc thực hiện bằng một hàm
#1. Nhập từ bàn phím dãy các số nguyên cách nhau bằng dấu cách. Chuyển các số này vào ds A
#2. Trích từ A ra một ds B gồm các số dương. In B ra
#3. Trích từ A ra một ds c gồm các số âm. In C ra



#Build hàm nhập ds số nguyên
'''def nhapDuLieu():
    numberList=input('Nhập các số nguyên cách nhau bằng dấu cách: ').split()
    # for i in range(len(numberList)):
    #     numberList[i]=int(numberList[i])
    # return numberList
    
    return [int(number) for number in numberList]
#hàm này không tối ưu vì lỡ nhập chữ cái, không phải số
A=nhapDuLieu()
print(f'Danh sách A: {A}')'''

def nhapDuLieu():
    while True:
        numberList=input('Nhập các số nguyên cách nhau bằng dấu cách: ').split()
        if not numberList:
            print('Chưa hợp lệ.')
            continue

        try:
            return [int(number) for number in numberList]
        
        except ValueError:
            print('Chỉ được nhập số nguyên.')


#list B lấy số dương của numberList
def getB(numberList):
    B=[]
    for i in numberList:
        if i>0:
            B.append(i)
    return B

#List C lấy số âm của numberList
def getC(numberList):
    return [number for number in numberList if number<0]

A=nhapDuLieu()
print(f'Danh sách A: {A}')
print(f'Danh sách B: {getB(A)}')
print(f'Danh sách C: {getC(A)}')
