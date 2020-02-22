# list , array mang
places =[ " Dai su quan" , " Benh vien", " Bai bien"] #init
print (places[1]) #read 

places.append(input(" enter new place  "))# create
places.index(" Benh vien")
print (places.index(" Benh vien")) 
places[0] ="Tieu su quan" #update
places.pop(2)   #delete by index
places.remove("Tieu su quan") #delete by value
temp = places[0]
places[0] = places[1]
places[1] = temp

for i in range(len(places)):
    print( places[i])


