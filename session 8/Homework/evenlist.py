def get_even_list(l):
    for index, value in enumerate(l):
        if value % 2 == 1:
            l.remove(value)
    return(l)
# z= get_even_list([1, 2, 5, -10, 9, 6])
# print (z)
