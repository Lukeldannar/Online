fail = False
try:
    num = int (input ("Enter a number below 50. "))
except:
    fail = True

if fail == True:
    print ("ERROR: INPUT NOT A NUMBER")
elif num > 49:
    print ("ERROR: INVALID NUMBER")
else:
    sub = 50
    while sub != num:
        print (sub)
        sub -= 1
    print (num)