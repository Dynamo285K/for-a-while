x=input("zadaj cislo")
x=int(x)
for i in range(1,x+1):
    if int(i)%3==0:
        print("cislo",i,"je delitelne tromi")
    else:
        print("cislo",i,"nie je delitelne tromi")

