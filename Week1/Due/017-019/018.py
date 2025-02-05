try:
    num = int (input ("Enter a number. "))
except:
    num = 21

if num < 10:
    print ("Too low.")
elif num < 21 and num > 9:
    print ("Correct.")
else:
    print ("Too high.")