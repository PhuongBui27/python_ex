CanFly=False
canSwim=False
CanChaseMouse=False
if CanFly:
    if canSwim:
        print('I am Duck')
    elif CanChaseMouse:
        print('I am a Eagle')
    else:
        print('I am Bird')
else:
    print('I am Chicken')
for i in range(0,10):
    if i%2==0:
        print(i)

workday=['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend=['Saturday','Sunday']
holiday=['30/04','01/05','02/09']
day='Monday'
date='30/09'
if day in weekend or date in holiday:
    print('Let\'s have fun')
else:
    print('Go to work')
if day=='Monday':
    print("meeting in new week")
elif day=='Tuesday':
    print('work in factory')
elif day=='Wednesday':
    print('design new product')




