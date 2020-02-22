Kho = {
    "HP": 20 ,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
    "ACER": 10,
    "TOSHIBA": 34,
    "FUJITSU": 87,
    "ALIENWARE": 35
}
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
for key,value in Kho.items():
    for key,val in Price.items():
        print(key,val* value )
        s =+ value* val
    break
print(s )
