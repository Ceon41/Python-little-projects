print("請輸入數字，直到9999結束")

count = 1 
minimum = int( input("請輸入第"+str(count)+"個數字：") )
userInput = minimum
while userInput != 9999:
    if userInput < minimum:
        minimum = userInput
    count += 1
    userInput = int( input("請輸入第"+str(count)+"個數字：") )
print("輸入的最小值為",minimum)    