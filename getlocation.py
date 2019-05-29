import geocoder
g = geocoder.ip('me')
coor = g.latlng
f = open("latlng.txt", "w+")

for c in coor:
    f.write(str(c))
    f.write("\n")
    print(str(c))
f.close()
