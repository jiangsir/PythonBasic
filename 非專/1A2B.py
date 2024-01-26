# 1A2B 猜數字遊戲
import random
ans = random.sample(range(1, 10), 4)
count = 0
while count < 8:
    guess = list(map(int, input("請輸入4個 1~9 的不同數字並以空白隔開: ").split()))
    count += 1
    a = b = 0
    for i in range(4):
        if ans[i] == guess[i]:
            a += 1
        elif guess[i] in ans:
            b += 1
    if a == 4:
        print("恭喜你答對了！共猜了", count, "次")
        break
    else:
        print(f"{a}A{b}B")
else:
    print(f"你已經猜錯8次了，答案是{ans}")
