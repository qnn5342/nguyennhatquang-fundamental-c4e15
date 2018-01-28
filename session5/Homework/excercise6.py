print ("Welcome to the Happy Farm!!!")
total = 1
listadd = []
for x in range(5):
    listadd.append(total)
    if x == 0:
        total = 1
    else:
        total = listadd[x] + listadd [x-1]
        # print (listadd)
        # print (total)
    print ("Month {0}: the farm has {1} couple(s)".format(x, total))
