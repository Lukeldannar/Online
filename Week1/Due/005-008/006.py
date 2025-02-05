stop = False

try:
    ini = int (input ("How many slices of pizza did you have? "))
    sub = int (input ("How many did you eat? "))
except:
    stop = True

if stop == False:
    ans = ini - sub
    print ("You now have",ans,"slices left.")