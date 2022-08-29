import random

while True:
    num = random.randint(-5,5)
    if num == 5:
        break
    try:
        result = 10/num
    except:
        print("發生除以 0 的情況")
    else:
        print("10 除以",num,"的結果是",result)