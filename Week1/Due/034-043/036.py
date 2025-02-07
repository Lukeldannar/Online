name = input ("Enter your name. ")

try:
    rep = int (input ("Enter a number. "))
except:
    print ("ERROR: INPUT NOT A NUMBER")

for i in range (rep):
    print (name)