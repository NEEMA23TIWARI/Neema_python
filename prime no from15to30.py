#WAP to print prime nos from 15 to 30

for i in range(15,31):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,"is prime")