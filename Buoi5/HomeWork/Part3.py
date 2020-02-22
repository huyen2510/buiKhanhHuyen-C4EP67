Kho = {
    "HP": 20 ,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
for key,value in Kho.items():
    print(key,value)
Kho['FUJITSU'] = 15
Kho['ALIENWARE'] = 5
print(sum(list(Kho.values())))  #sum(allvalue)

