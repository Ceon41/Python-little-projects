fobj = open("25.Data.csv","r",encoding="utf-8")
content = fobj.read()
fobj.close()

print(content)
content = content + "趙六,女,23\n"

try:
    fobj = open("24_3data.csv","w",encoding="utf-8")
    fobj.write( content )
    fobj.close()
except:
    print("您的檔案恐已被 Excel 開啟，請關閉 Excel 才能寫入")
else:
    print("檔案已寫入完成")





