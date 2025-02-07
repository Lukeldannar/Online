ask = input ("Do you want to count up or down? ").lower()

if ask == "up":
    fail = False
    try:
        num = int (input ("Enter number you want to count up to from 1. "))
    except:
        fail = True

    if fail == True:
        print ("ERROR: INPUT NOT A NUMBER")
    elif num < 1:
        print ("ERROR: NUMBER WILL CAUSE LOOP TO NEVER END")
    else:
        add = 1
        while add != num:
            print (add)
            add += 1
        print (num)

elif ask == "down":
    fail = False
    try:
        num = int (input ("Enter number you want to count down to from 20. "))
    except:
        fail = True

    if fail == True:
        print ("ERROR: INPUT NOT A NUMBER")
    elif num > 20:
        print ("ERROR: NUMBER WILL CAUSE LOOP TO NEVER END")
    else:
        sub = 20
        while sub != num:
            print (sub)
            sub -= 1
        print (num)

else:
    print ("I don't understand")