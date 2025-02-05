word = input ("Enter a word. ").lower()

if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
    word = word + "way"
    print (word)
else:
    num_cha = len (word) - 1
    print (num_cha)
    list = []
    tot = -1
    for i in word:
        tot += 1
        if tot == 0:
            list.append (word[tot+1])
        elif tot == (num_cha):
            list.append (word[0])
        else:
            list.append (word[tot+1])
    fin = None
    for i in list:
        None
    print (list)