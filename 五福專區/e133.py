# 讀取進來之後，用 strip 清除掉前後的不可見字元
s = input().strip()
count = 0
for i in s: # 對 s 字串進行遍歷
    if i == '1': # 判斷是否是 1(這是字元，不是數字)
        count = count + 1

if count%2==0:
    print(s+'1') 
else:
    print(s+'0')