import random

pwd = random.sample(range(0,10),4)
A = 0
B = 0

while A!=4:
    num = input("請輸入 4 個數字：")
    while len(num) != 4 or len(set(num)) != 4:
        num = input("請輸入 4 個數字，且數字勿重複：")
    
    list1 = list(map(int,list(num)))
    A = 0
    B = 0
    for i in list1:
        if i in pwd:
            if list1.index( i ) == pwd.index( i ):
                A += 1
            else:
                B += 1
                
    print(num,"：",A,"A",B,"B",sep="")
    
print("你猜對了，密碼是",num)
