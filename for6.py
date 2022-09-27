zaciatok=input("zadaj mi cislo")
koniec=input("zadaj mi cislo")
zaciatok=int(zaciatok)
koniec=int(koniec)
y=0

for i in range(zaciatok,koniec+1):
  if i%8==0:
    y=y+1
print("v intervale od",zaciatok,"az",koniec,"je pocet cisel delitelnych osmimi:",y)