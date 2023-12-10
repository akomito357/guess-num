# 產生一個隨機整數1～100（不要印出來）
# 讓使用者重複輸入數字去猜
# 猜對的話印出「終於猜對了！」
# 猜錯的話要告訴他比答案大/小

import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1 # count = count + 1
    guess = input('你猜的數字是：')
    guess = int(guess)
    if guess == r:
        print('終於猜對了！')
        print('這是你猜的第', count, '次')
        break
    elif guess > r:
        print('比答案大')
    elif guess < r:
        print('比答案小')
    print('這是你猜的第', count, '次')