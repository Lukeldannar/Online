name = input ("Enter your first name. ")
n1 = len (name)

if n1 < 5:
    sur = input ("Enter your surname. ")
    to = (name + sur).upper()
    print (to)
elif n1 == 5 or n1 > 5:
    name = name.lower()
    print (name)