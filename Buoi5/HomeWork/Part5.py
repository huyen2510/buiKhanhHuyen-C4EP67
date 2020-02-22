Price = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000
}
Kho = {
    "HP": 20 ,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
    "ACER": 10,
    "TOSHIBA": 90,
    "FUJITSU": 80,
    "ALIENWARE": 15
}
print('Gia tri 5 máy ASUS: ',5*Price['ASUS'] )
a = input(" Nhập máy bạn muốn mua: ")
b = input(" Nhập số lượng máy đó: ")
print("Giá trị ",b,"máy " , a ,"la: ", int(b)*Price[a])
Kho[a] = Kho[a] - int(b)
print(Kho)
