try:
    num = int (input ("Enter 1, 2, or 3. "))
except:
    num = 9

if num == 1:
    print ("Thank you.")
elif num == 2:
    print ("Well done.")
elif num == 3:
    print ("Correct")
else:
    print ("Error message")