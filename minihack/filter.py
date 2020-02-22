# # b4
# a= [1,3,4,9,8,4]
# final_list = list(filter(lambda x: (x%2 != 0) , a)) 
# print(final_list) 

# #b5
# a = [int(x) for x in input().split()]
# print(a)

# b6: index
list1= [ "ST"," BĐ" , "BTL" ,"CG" , "ĐĐ", "HBT"]
list2 = [ 150.300,247.100, 333.300,266.800,420.900,318.000]
a = list2.index(max(list2))
print(a)
b = list2.index(min(list2))
print(b)
# from index to name
print("Quan co dan so nhieu nhat:",list1[a])
print("Quan co dan so it nhat",  list1[b])

Dientich= [ 117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
MatDo = []
for i in range(6) :
    c = list2[i]/Dientich[i]
    print(list2[i]/Dientich[i])
    MatDo.append(c)
print(MatDo)

# mat do dan cu trung binh
m = sum(MatDo)
print(m)
n = len(list1)
print(n)
tb = m/ n 
print(" Mat Do Dan Cu TB: ", tb)


