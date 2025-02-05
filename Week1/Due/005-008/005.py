stop = False
   
try:
    num1 = int (input ("Give me a number. "))
    num2 = int (input ("Give me a seacond number. "))
    num3 = int( input ("Give me a third number. "))
except:
    stop = True

if stop == False:
    ans = (num1 + num2) * num3
    print ("The total is",ans)