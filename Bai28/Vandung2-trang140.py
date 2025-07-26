#Viết CT nhập vào 3 số tự nhiên day, month, year cách nhau bởi dấu cách biểu diễn ngày tháng năm nào đó. Kiểm tra và in ra thông báo số liệu đã nhập vào đó có hợp lệ hay chưa


#Kiểm tra năm nhuận
def leap_year(year):
    return ((year%4==0 and year%100!=0) or year%400==0)



def is_valid_date(day,month,year):
    #Kiểm tra năm
    if year<1:
        return False
    
    #Kiểm tra tháng
    if month<1 or month>12:
        return False
    
    #Cập nhật số ngày trong các tháng 1,2,...,12
    day_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]

    #Cập nhật số ngày cho tháng 2 nếu năm nhuận
    if leap_year(year):
        day_in_month[1]=29

    #Kiểm tra ngày
    if day<1 or day>day_in_month[month-1]:
        return False
    
    return True


def main():
    while True:
        try:
            values=input('Nhập ngày, tháng, năm (cách nhau bởi dấu cách): ').split()
            if len(values)!=3:
                print('Chưa hợp lệ.')
                continue
            day, month, year=map(int,values)
            break
        except ValueError:
            print('Chưa hợp lệ.')

    if is_valid_date(day,month,year):
        return f'Ngày {day}/{month}/{year} hợp lệ.'
    else:
        return f'Ngày {day}/{month}/{year} không hợp lệ.'

print(main())
