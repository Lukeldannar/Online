name = input ("Enter your name. ")

fail = False
try:
    rep = int (input ("Enter a number. "))
except:
    fail = True
if fail == False:
    for h in range (rep):
        for i in name:
            print (i)