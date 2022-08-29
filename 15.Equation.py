def equation(a, b, c):
    d = b**2-4*a*c
    if d >= 0:
        m = (-b+d**0.5)/(2*a)
        n = (-b-d**0.5)/(2*a)
        return str(m)+","+str(n)
    else:
        return "無解"
    
a = eval( input("請輸入方程式係數 a："))
b = eval( input("請輸入方程式係數 b："))
c = eval( input("請輸入方程式係數 c："))
print( "方程式解為"+equation(a,b,c) )