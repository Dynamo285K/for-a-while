x=input("zadaj mi cislo")
x=int(x)
y=0

for i in range(1,x+1):
  if i%2==0:
    y=y+1
print("vysledok je:",y)