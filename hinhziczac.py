soduong=int(input('Moi ban nhap so duong zic zac:'))
sodiem=int(input('Moi ban nhap so diem zic zac:'))
for i in range(0,sodiem,1):
    for j in range(0,(soduong*(sodiem-1)+1),1):
        for k in range(1,soduong,1):
            if k%2!=0:
                if ((i+j)==(sodiem-1)*k) or (j-i)==(sodiem-1)*k:
                    print('*',end='')
                    k=soduong+1
        else:
            print('',end='')
    print('')