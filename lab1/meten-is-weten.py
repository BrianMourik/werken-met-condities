a = int(input("A: "))
b = int(input("B: "))

if (a > b):

   max = a
   min = b

   print("a is het grootste getal " + str(max))
   print(" ")
   print("het minimum is:" + str(min))
   print("het maximum is:" + str(max))


elif (a < b):

    min = a
    max = b

    print("a is het kleinste getal " + str(min)) 
    print(" ")
    print("het minimum is:" + str(min))
    print("het maximum is:" + str(max))


else:
    print("a en b zijn even groot")