stop = False

try:
    age = int (input ("What is your age? "))
except:
    stop = True

if stop == False:
    if age > 18 or age == 18:
        print ("You can vote.")
    elif age == 17:
        print ("You can learn to drive.")
    elif age == 16:
        print ("You can buy a lottery ticket.")
    elif age < 16:
        print ("You can go Trick-or-Treating.")
    else:
        print ("ERROR")