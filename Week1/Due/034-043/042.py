total = 0

for i in range (5):
    inc = True
    try:
        num = int (input ("Enter a number. "))
    except:
        inc = False
    if inc == False:
        print ("ERROR: INPUT INVALID")
    else:
        ask = input ("Do you want to add this number to the total? ").lower()
        if ask == "yes" or ask == "y":
            total += num
print (total)