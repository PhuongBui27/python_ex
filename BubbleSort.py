import random
char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
numberchar=random.randint(5,10)
list=random.sample(char,numberchar)
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i]< list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)