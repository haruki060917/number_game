import random

answer = random.randint(100, 999)
max_attempts = 7

print("3桁の数字当てゲームです")
print(f"{max_attempts}回以内に正解してください")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"{attempt}回目の入力: "))

    if guess == answer:
        print("正解")
        break
    else:
        print("不正解")
else:
    print(f"正解は{answer}でした")