h=float(input("請輸入身高 （公分）"))
w=float(input("請輸入體重 （公斤）"))

h=h/100.0
BMI=w/(h**2)

print("身高：",h)
print("體重：",w)
print("BMI:",str(round(BMI,2)))




