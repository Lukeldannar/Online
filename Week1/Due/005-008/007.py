stop = False

name = input ("What is your name? ")

try:
    age = int (input ("What is your age? "))
except:
    stop = True

if stop == False:
    newage = age + 1
    print (name,"next birthday you will be",newage)