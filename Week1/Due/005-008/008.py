stop = False

try:
    tot = int (input ("What is the total bill? "))
    num = int (input ("How many people are you dinning with? "))
except:
    stop = True

if stop == False:
    pay = tot / num
    pay = round (pay,2)
    print ("Each person must pay",pay)