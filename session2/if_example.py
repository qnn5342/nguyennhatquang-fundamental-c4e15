yob = int(input("what year were u born?:"))
age = 2018 - yob
print   ("age = ", age)

if age < 10:
    print ("Baby")
elif age< 18:
    print ("teenager")
else:
    print ("adults")
