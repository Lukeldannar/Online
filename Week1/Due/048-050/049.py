atm = 0
compnum = 50
num = 0

while num != compnum:
    atm += 1
    try:
        num = int (input ("Quess the number. "))
    except:
        num = "no"
    if num == "no":
        print ("""ERROR: NUMBER NOT GIVEN
    Attempt not added""")
        atm -= 1
    elif num < 50:
        print ("Too low. Try again.")
    elif num > 50:
        print ("Too high, try again")

print ("Well done. You took",atm,"attempts")