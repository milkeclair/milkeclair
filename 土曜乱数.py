import random
random_number = 0
while True:
    random_number = random.randint(0,6)
    if random_number == 5:
        print("土曜日！")
        break
    if random_number == 0:
        print("月曜日！")
        continue
    if random_number == 1:
        print("火曜日...")
        continue
    if random_number == 2:
        print("水曜日")
        continue
    if random_number == 3:
        print("木曜日")
        continue
    if random_number == 4:
        print("金曜日！")
        continue
    if random_number == 6:
        print("日曜日")
        continue