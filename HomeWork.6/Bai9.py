# l = [1,4,5,-1,10]
newlist = []
def get_even_list(l):
    for i in range(len(l)):
        if l[i]% 2 == 0:
            a = l[i]
            newlist.append(a)
    return newlist

# print(get_even_list([1, 10, -3, -4]))