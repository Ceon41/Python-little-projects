print("請輸入數字，直到9999結束")

count = 1
while True:
    num = input("請輸入第"+str(count)+"個數字：")
    if num == '9999':
        break
    result = ""
    for i in range( len( num ) ):
        result = num[i] + result
    print("反轉的數字為：",result)
    count += 1
