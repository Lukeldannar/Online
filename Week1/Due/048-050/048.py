count = 0
inv = "yes"

while inv == "yes" or inv == "y":
    name = input ("Enter the name of who you want to add to the party. ")
    print (name,"has been invited to the party")
    count += 1
    inv = input ("Do you want to invite more people? ").lower()

print (count,"people are comming to the party!")