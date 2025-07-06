#Cho dãy số lst. Viết chương trình thực hiện
#a) Xóa đi phần tử chính giữa dãy nếu số phần tử của dãy là số lẻ
#b) Xóa đi 2 phần tử chính giữa dãy nếu số phần tử của dãy là số chẵn




'''lst=[1, 4, 3, 1, 2, 2]
# print(len(lst))
n=len(lst)
if n%2==1:
    mid=n//2
    del(lst[mid])
    print(f'Số phần tử lẻ, xóa đi phần tử chính giữa còn lại: {lst}')
else:
    mid1=n//2-1
    mid2=n//2
    del(lst[mid2])
    del(lst[mid1])
    print(f'Số phần tử chẵn, xóa đi 2 phần tử chính giữa còn lại: {lst}')'''


def delMiddleNumber(lst):
    n=len(lst)
    if n%2==1:
        mid=n//2
        del(lst[mid])
        print(f'Số phần tử lẻ, xóa đi số ở chính giữa, danh sách còn lại: {lst}')
    else:
        mid1=n//2 - 1
        mid2=n//2
        del(lst[mid2])
        del(lst[mid1])
        print(f'Số phần tử chẵn, xóa đi 2 số ở chính giữa, danh sách còn lại: {lst}')

lst=[1, 4, 3, 1, 2, 2, 3]
delMiddleNumber(lst)
