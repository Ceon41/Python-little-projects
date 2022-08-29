import random

pwd = random.randint(0,9)

guessNum = int( input("請輸入數字(0~9)：") )
while guessNum != pwd:
    guessNum = int( input("估錯啦，再估(0~9)："))
print("估岩啦，密碼就是",pwd)