list1 = input("請輸入第 1 個數組：").split(" ")
tuple1 = tuple(map(int,list1))
list2 = input("請輸入第 2 個數組：").split(" ")
tuple2 = tuple(map(int,list2))

print("數組合併:",tuple1+tuple2)
print("合併後排序:",sorted(tuple1+tuple2))
