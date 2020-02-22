# person = ["Đức", 96,'Ha Noi' , "Son La",'dev', False, True]
person = {
    'name': 'Huyen', 
    ' yob': 2000, 
    'address': 'Ha Noi'
}
# dict:
# {
    # 'key': value, 
    
# }
# print(person)
# print(person['name'])
Jennie ={
    'nickname' : 'jen',
    'yob' : 96,
    'musictype': 'dance',
    'love': 3000,
    'pet':'kai, kuma'
}
# print(Jennie['love'])
# cach2: read All
# key = input()
# print(person[key])
person['gender'] = 'female' #create
person['address'] = 'Da Lat' #update
# cac key k dc trung nhau, neu key giong nhau se lay key cuoi cung
del person[' yob'] 
if 'name' in person:
    print(person['name'])
for key,value in person.items():
    print(key,value)