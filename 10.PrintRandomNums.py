import random

while True:
    num = random.randint(1,20)
    if num == 11:
        break
    if num%5 == 0:
        continue
    print( num )
print("隨機數字中11便結束。")