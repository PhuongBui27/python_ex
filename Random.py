import random
random.SystemRandom()
items=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
thumon=random.sample(items,1)
print('Thu mon:',thumon)
items2=list(set(items)-set(thumon))
hauve=random.sample(items2,4)
print('Hau ve:',hauve)
items3=list(set(items2)-set(hauve))
tienve=random.sample(items3,4)
print('Tien ve:',tienve)
items4=list(set(items3)-set(tienve))
tiendao=random.sample(items4,2)
print('Tien dao:',tiendao)
