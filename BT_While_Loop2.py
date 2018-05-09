normal=['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín','mười']
special=['mươi','lăm','mốt','lẻ','linh']
normal2=['Mười','Hai mươi','Ba mươi','Bốn mươi','Năm mươi','Sáu mươi','Bảy mươi','Tám mươi','Chín mươi']
number=int(input('Nhập vào một số nguyên: '))
for i in range(len(normal)):
    if number==i:
        print('Giá trị bằng chữ của %d là: %s' % (number,normal[i]))
    #i+=1
if number >10 and number <20:
    for i in range(len(normal)):
        if number == 10+i:
            print('Giá trị bằng chữ của %d là: Mười %s' % (number, normal[i]))
        #i += 1
if number >=20 and number <99:
    for i in range(len(normal)):
        if number//10 == i and number % 10 == 1:
            print('Giá trị bằng chữ của %d là: %s mươi mốt' % (number, normal[i]))
            break
        elif number//10==i and number%10==0:
            print('Giá trị bằng chữ của %d là: %s mươi' % (number, normal[i]))
            break
        if number//10==i:
            for j in range(len(normal)):
                if number%10==j:
                    print('Giá trị bằng chữ của %d là: %s mươi %s' % (number, normal[i],normal[j]))

if number >=100 and number <=999:
    for i in range(len(normal)):
        if number//100 == i:
            for j in range(len(normal)):
                if number%100==j and j <=9 and j >0:
                    print('Giá trị bằng chữ của %d là: %s trăm linh %s' % (number, normal[i],normal[j]))
                    break
        if number//100==i and number%100==0:
            print('Giá trị bằng chữ của %d là: %s trăm' % (number, normal[i]))
            break
        if number//100==i:
            if number%100 >10 and number%100 < 20:
                for j in range(len(normal)):
                    if number%100 == 10 + j:
                        print('Giá trị bằng chữ của %d là: %s trăm mười %s' % (number, normal[i],normal[j]))
                break
            if number % 100 == 10:
                print('Giá trị bằng chữ của %d là: %s trăm mười' % (number, normal[i]))
                break

        if number // 100 == i and number%100 >= 20 and number%100 <= 99:
            for j in range(len(normal)):
                if (number % 100)%10 == 1 and (number % 100)//10 == j:
                    print('Giá trị bằng chữ của %d là: %s trăm %s mươi mốt' % (number, normal[i],normal[j]))
                    break
                elif (number % 100)%10 == 0 and (number % 100)//10 == j:
                    print('Giá trị bằng chữ của %d là: %s trăm %s mươi' % (number, normal[i],normal[j]))
                    break
                for k in range(len(normal)):
                    if (number % 100) % 10 == k and (number % 100) // 10 == j:
                        print('Giá trị bằng chữ của %d là: %s trăm %s mươi %s' % (number, normal[i], normal[j],normal[k]))
                        break

if number >=1000 and number<=9999:
    du=number%1000
    ng=number//1000
    for i in range(len(normal)):
        if ng==i:
            if du==0:
                print('Giá trị bằng chữ của %d là: %s nghìn'% (number,normal[i]))
                break

            '''for k in range(len(normal)):
                if du%10==1 and du//10 == k and du>20 and du<=99:
                    print("Giá trị bằng chữ của %d là: %s nghìn không trăm %s mươi mốt" % (number, normal[i], normal[k]))
                    break
            for j in range(len(normal)):
                if du==j and du<=9 and du>=1:
                    print("Giá trị bằng chữ của %d là: %s nghìn không trăm linh %s" % (number,normal[i],normal[j]))
                    break
                if du%10==j and du>10 and du<20:
                    print("Giá trị bằng chữ của %d là: %s nghìn không trăm mười %s" % (number, normal[i], normal[j]))
                    break
                if du%10==0 and du//10==j and du>20 and du<=99:
                    print("Giá trị bằng chữ của %d là: %s nghìn không trăm %s mươi" % (number, normal[i], normal[j]))
                    break

                for k in range(len(normal)):
                    if du%10==j and du//10==k and du>20 and du<=99 and j!=1 and j!=0:
                        print("Giá trị bằng chữ của %d là: %s nghìn không trăm %s mươi %s" % (number, normal[i],normal[k], normal[j]))
                        break
                    break'''
            # Hàng trăm

            for h in range(len(normal)):
                if du//100==h:
                    if du%100 == 0:
                        print('Giá trị bằng chữ của %d là: %s nghìn %s trăm' % (number, normal[i],normal[h]))
                        break
                    for k in range(len(normal)):
                        if (du%100) % 10 == 1 and (du%100) // 10 == k and k!=0:
                            print("Giá trị bằng chữ của %d là: %s nghìn %s trăm %s mươi mốt" % (number, normal[i],normal[h], normal[k]))
                            break

                    for j in range(len(normal)):
                        if du%100 == j and du%100 <= 9 and du%100 >= 1:
                            print("Giá trị bằng chữ của %d là: %s nghìn %s trăm linh %s" % (number, normal[i],normal[h], normal[j]))
                            break
                        if (du%100) % 10 == j and (du%100) > 10 and (du%100) < 20:
                            print("Giá trị bằng chữ của %d là: %s nghìn %s trăm mười %s" % (number, normal[i],normal[h], normal[j]))
                            break
                        if (du%100) % 10 == 0 and (du%100) // 10 == j and (du%100) > 20 and (du%100) <= 99:
                            print("Giá trị bằng chữ của %d là: %s nghìn %s trăm %s mươi" % (number, normal[i],normal[h], normal[j]))
                            break
                        for k in range(len(normal)):
                            if (du%100) % 10 == j and (du%100) // 10 == k and (du%100) > 20 and (du%100) <= 99 and j != 1 and j != 0:
                                print("Giá trị bằng chữ của %d là: %s nghìn %s trăm %s mươi %s" % (number, normal[i], normal[h],normal[k], normal[j]))
                                break
                            break
                        break
                    break
                break
            break
        break



if number >=10000 and number<=99999:
    du = number % 10000
    ng = number // 10000










