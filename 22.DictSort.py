print("請輸入顏色詞典，當 key 輸入 end 時結束")
dict1 = dict()
while True:
    key = input("Key: ")
    if key=='end':
        break
    value = input("Value: ")
    dict1[key] = value
    
for i in sorted(dict1.keys()):
    print(i,": ",dict1[i],sep="")