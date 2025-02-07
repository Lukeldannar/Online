name = input ("Enter your name. ")

fail = False
try:
    num = int (input ("Enter a number. "))
except:
    fail = True

if fail == True:
    print ("ERROR: INPUT NOT A NUMBER")
elif num < 10:
    for i in range (num):
        print (name)
else:
    for i in range (3):
        print ("Too high")