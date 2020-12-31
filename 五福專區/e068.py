N = int(input()) # 讀取第一個整數 N

max = -1
ansx = -1
ansy = -1
for _ in range(N): # 用一個 for 迴圈將接下來的 N 行讀取進來。
    x, y = map(int, input().split()) # 讀取進來直呼直接轉成整數 x, y。
    if x * y > max: # 如果找到比目前 max 還大的矩形的化，就更換 max 並且將答案記錄下來。
        max = x * y
        ansx = x
        ansy = y
print(ansx, ansy)