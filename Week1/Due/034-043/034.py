try:
    num = int ( input ("""       1) Square
       2) Triangle
"""))
except:
    num = 0

if num == 1:
    fail = False
    try:
        len = int (input ("Enter the length of one side. "))
    except:
        print ("ERROR: INPUT NOT A NUMBER")
        fail = True
    if fail == False:
        area = len ** 2
        print (area)
elif num == 2:
    fail = False
    try:
        base = int (input ("Enter base of the triangle. "))
        hei = int (input ("Enter height of the triangle. "))
    except:
        print ("ERROR: INPUT NOT A NUMBER")
        fail = True
    if fail == False:
        area = (base * hei) / 2
        print (area)
else:
    print ("ERROR: UNSUPPORTED INPUT")