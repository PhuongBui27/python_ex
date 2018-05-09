'''correctNumber=58
while True:
    number=int(input("Guess a number betwen 0 and 100: "))
    if correctNumber==number:
        print('Cool you have found correct number ',number)
    elif correctNumber >number:
        print('Correct number is higher than your input ',number)
    else:
        print('Correct number is less than your input',number)'''
# Phần 2: Tìm N số nguyên tố dầu tiên, in ra mỗi hàng 10 số và căn lề bên phải

number0fPrimes = 500 #Số lượng số nguyên tố cần tìm ra
count0fPrimes=0 #Biến đếm
number0fPrimesPerLine=10 #Số lượng số nguyên tố in ra trong 1 dòng
primeInLineCount=0 #Biến đếm - đếm sô nguyên tố trên 1 dòng
i=1
while count0fPrimes < number0fPrimes:
    for j in range(2,i//2):
        if i%j==0:
            break
    else:
        count0fPrimes+=1
        print("%6d" % (i), end="")
        primeInLineCount +=1
        if primeInLineCount >= number0fPrimesPerLine:
            print("") # in dấu xuống dòng
            primeInLineCount=0
    i+=1