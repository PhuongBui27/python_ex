import sys
from termcolor import colored, cprint
tasks=['Get requirements','Design','Code','Test','Ship','Fix Bug']
for task in tasks:
    print(task)
for i in range(len(tasks)):
    print('task %d %s' % (i,tasks[i]))
name='Jame Cook'
for char in name:
    print(char)
numbers=[12,16,17,18,20,22,35]
for i in numbers:
    if i%2==1:
        continue
    print(i)
print('done')
for num in range(1,20):
    for i in range(2,num):
        if num %i==0:
            j=num/i
            print('%d equals %d * %d' % (num,i,j))
            break #thoat khoi vong lap trong cung
    else:
        #print('%d is a prime number' %(num))
        cprint(str(num)+ 'is a prime number','red','on_yellow')

for i in range(10,-11,-1):
    print(i)

i=0
while i<100:
    print(i)
    i +=5
numbers=[12,16,18,24,29,30]
for i in numbers:
    if i%2==1:
        break
    print(i,'',end='')