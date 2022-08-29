def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)
    
a,b = input("請輸入兩個數字，中間以逗點做分隔：").split(',')
a = int(a)
b = int(b)
print( a,"與",b,"的最大公因數為",gcd(a,b) )