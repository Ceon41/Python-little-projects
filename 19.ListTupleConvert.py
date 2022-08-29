list1 = list()
count = 1
while True:
    num = int( input("請輸入第 "+str(count)+" 個數字："))
    if num == -9999:
        break
    list1.append( num )
    count += 1
    
tuple1 = tuple(list1)
print( tuple1 )
print("長度：",len(tuple1))
print("最大值：",max(tuple1))
print("最小值：",min(tuple1))
print("總和：",sum(tuple1))








