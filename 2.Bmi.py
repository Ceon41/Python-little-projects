sex = input("請問你的性別是(M/F)：")
height = eval( input("請問你的身高是 (cm)：") )
weight = eval( input("請問你的體重是 (kg)：") )

bmi = weight / (height/100)**2

if sex=='M':
    if bmi > 25:
        print("體重過重")
    elif bmi < 20:
        print("體重過輕")
    else:
        print("身材適中")
else:
    if bmi > 22:
        print("體重過重")
    elif bmi < 18:
        print("體重過輕")
    else:
        print("身材適中")









