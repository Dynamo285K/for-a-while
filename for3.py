x=input("zadaj mi cislo")
x=int(x)
y=0

for i in range(1,x+1):
  if i%7==0 and i%4==0:
    y=y+1
print("pocet cisel delitelnych 4 a 7 je:",y)