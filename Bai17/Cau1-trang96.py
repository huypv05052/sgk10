#Viết lệnh thực hiện việc đổi số giây ss cho trước sang số ngày, giờ, phút, giây và in kết quả ra màn hình
#EX: ss=684500 thì kết quả in ra: 684500ss = 7 ngày 22h 8 phút 20ss
#suggest: 1 ngày = 86400ss, 1h = 3600ss, 1 phút= 60 ss


s1 = int(input('Nhập số ss ban đầu: '))
ngay = s1//86400
s2 = s1%86400
gio = s2//3600
s3 = s2%3600
phut = s3//60
giay = s3%60
print(f'{s1}s = {ngay} ngày {gio} giờ {phut} phút {giay}s')
