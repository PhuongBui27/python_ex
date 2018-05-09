name='abc'
name2='ABC'.lower()
if name==name2:
    print("Both are equal")
else:
    print('Not equal')
if name is name2:
    print('Identical')
else:
    print('Not identical')
print(id(name),id(name2))
if name is not name2:
    print('name is not name2')
x=2/7
print('x')
y=2/7
print('y')
if x is y:
    print('x is y')
if x==y:
    print('x is equal to y')
else:
    print('x is not equal to y')
if abs(x-y)<0.0000001:
    print('x is similar to y')

