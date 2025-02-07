fail = False

try:
    num = int (input ("Enter a number between 1 and 12. "))
except:
    fail = True

if fail == True:
    print ("ERROR: INPUT NOT A NUMBER")
elif num < 0 or num > 12:
    print ("ERROR: INVALID NUMBER")
else:
    print ("1 x",num,"=",num)
    print ("2 x",num,"=",num * 2)
    print ("3 x",num,"=",num * 3)
    print ("4 x",num,"=",num * 4)
    print ("5 x",num,"=",num * 5)
    print ("6 x",num,"=",num * 6)
    print ("7 x",num,"=",num * 7)
    print ("8 x",num,"=",num * 8)
    print ("9 x",num,"=",num * 9)
    print ("10 x",num,"=",num * 10)
    print ("11 x",num,"=",num * 11)
    print ("12 x",num,"=",num * 12)