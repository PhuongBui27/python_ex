i=0
j=0
x = [1, 2, 9]
y = [4, 5, 6]
for i in range (1,x[i]):
    for j in range (1,y[j]):
        if x[i]+y[j] <=10:
            zipped = zip(x, y)
            print(list(zipped))
            break



