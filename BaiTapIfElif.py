# Bài 1
score=75
if score >= 90:
    print('Grade is A')
elif score >=80:
    print('Grade is B')
elif score >=70:
    print('Grade is C')
elif score >= 60:
    print('Grade is D')
else:
    print('Grade is F')

#Bài 2
Weight=100
Height=50
Kilogram=Weight*0.45359237
Meter=Height*0.0254
print('Chieu cao cua ban la: %.2f Meter'% (Meter))
print('Can nang cua ban la: %.1f Kg' % (Kilogram))
BMI=Kilogram/(Meter*Meter)
print('Chi so BMI cua ban la: %.1f' % (BMI))
if BMI<18.5:
    print('Tinh trang cua ban: Underweight')
elif BMI<25 and BMI>= 18.5:
    print('Tinh trang cua ban: Normal')
elif BMI<30 and BMI>=25:
    print('Tinh trang cua ban: Overweight')
else:
    print('Tinh trang cua ban: Obese')









