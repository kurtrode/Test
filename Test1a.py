import random
while True:
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,10)
    f=str(a)+" + "+str(b)+" + "+str(c)
    g=str(a)+" + "+str(b)+" - "+str(c)
    h=str(a)+" - "+str(b)+" + "+str(c)
    i=str(a)+" - "+str(b)+" - "+str(c)
    items = [1, 2, 3, 4]
    def rand():
        random.choice(items)
    def again():
        x = "y"
        last = raw_input("Do you want to continue? y/n: ")
        if last == x:
            break
        else:
            quit()
    if random.choice(items) == 1:
        j = a+b+c
        if j >= 0:
            print (str(a)+" + "+str(b)+" + "+str(c))
            z = input()
            if z == j:
                print ("Correct")
                again ()
            else:
                print ("Sorry, no ")
                again()
        else:
            continue
    elif random.choice(items) == 2:
        j = a+b-c
        if j >= 0:
            print (str(a)+" + "+str(b)+" - "+str(c))
            z = input()
            if z == j:
                print ("Correct")
            else:
                print ("Sorry, no")
        else:
            continue
    elif random.choice(items) == 3:
        j = a-b+c
        if j >= 0 and a-b > 0:
            print (str(a)+" - "+str(b)+" + "+str(c))
            z = input()
            if z == j:
                print ("Correct")
            else:
                print ("Sorry, no")
        else:
            continue
    elif random.choice(items) == 4:
        j = a-b-c
        if j >= 0:
            print (str(a)+" - "+str(b)+" - "+str(c))
            z = input()
            if z == j:
                print ("Correct")
            else:
                print ("Sorry, no")
        else:
            continue
