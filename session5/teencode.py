engcode = {
"xem": "watch",
"phê": "high",
"bongda": 'football'
}
# iterate by key
for key in engcode:
    print(key, end = ' ')
# iterate by value
# print (*codex)
# for x in engcode.values():
#     print(x)
# # iterate by item
# for x,y in engcode.items():
#     print (x,y)

# create = update

print ("*"*10)

insert = input("enter a word above to get english: ")

if insert in engcode:
    print (engcode[insert])
else:
    insert2 = (input ("Not found! Do you want to contribute this word? (Y/N)")).lower()
    if insert2 == 'y':
        insert3 = input("please input your translation")
        engcode[insert] = insert3
        print (engcode)
    else:
        pass
