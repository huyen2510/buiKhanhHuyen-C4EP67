def is_inside(point,regtangle):
    if point[0] > regtangle[0] and point[1] > regtangle[1]:
        if regtangle[2] > (point[0]-regtangle[0]) and regtangle [3] > (point[1]-regtangle[1]):
            result = True
        else:
            result = False
    else:
        result = False
    print(result)
    return(result, point, regtangle)

inside = bool(is_inside([200,120],[140,60,100,200]))
if inside == True:
    print("Your function is correct")
else:
    print("Bugs detected")
is_inside([200,120],[140,60,100,200])