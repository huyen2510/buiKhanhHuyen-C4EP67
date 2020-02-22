Kho = {
    "HP": 20 ,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
Kho['TOSHIBA'] = 10
a = input( " Nhap may ban muon them: ")
b = input(" Nhap so luong ")
Kho[a] = b
Kho["DELL"] = 60
Kho["MACBOOK"] = 2
print(Kho)

