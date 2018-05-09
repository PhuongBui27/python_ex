'''number=int(input('Input an odd number: '))
if number %2==0:
    print('Sorry, the number you enter is even number')
    number=int(input('Input an odd number: '))
if number%2==1:
    for i in range(number,0,-2):

        for j in range(1,(number+1)//2):
            print('',end='')
        for k in range(number-i, number):
            print(i,end='')
        print('')

# Bài 2:
for i in range(1,100):
    if i%3==0:
        print('%3d' % (i),end='')
'''
numbers=[1,3,5,7,9,11,14,15]
for i in numbers:
    if i%2==0:
        print('Found even')
        break
print('All are odd numbers')



