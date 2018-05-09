n1=int(input("Enter first integer: "))
n2=int(input("Enter second integer: "))
UCLN=1
k=2
if n1 < 0 or n2<0:
    print('Xin hay nhap so nguyen duong')
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))

    if n1==0 and n2==0:
        print('Loi Chia 0')
    elif n1==0 and n2 != 0:
        print('So chia lon nhat cua %d va %d la: %d '%(n1,n2,n2))
    elif n2 == 0 and n1 != 0:
        print('So chia lon nhat cua %d va %d la: %d '% (n1, n2, n1))

    elif n1 != n2 and n1>0 and n2>0:

        while k<=n1 and k<=n2:
            if n1%k==0 and n2%k==0:
                UCLN=k
            k+=1
        print("So Chia lon nhat cua hai so tren la: ", UCLN)







