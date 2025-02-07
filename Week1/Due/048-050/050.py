num = 0
x = True

while x == True:
    try:
        num = int (input ("Enter a number. "))
    except:
        num = "no"
    if num == "no":
        print ("ERROR: NUMBER NOT GIVEN")
    elif num < 10:
        print ("Too low. Try again.")
    elif num > 20:
        print ("Too high, try again")
    else:
        break

print ("Thank you")