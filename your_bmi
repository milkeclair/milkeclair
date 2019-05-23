while True:
    try:
        h = input("身長(cm)を半角数字で入力して下さい。:")
        if len(h) == 0:
            break
        h = float(h)
        h = h / 100
        w = input("体重(kg)を半角数字で入力して下さい。:")
        if len(w) == 0:
            break
        w = float(w)
    except:
        print("[Please try again]")
        continue
    bmi = w / pow(h,2)
    print("BMI[{:.2f}]です。".format(bmi))
    if bmi < 18.50:
        print("やせぎみです。")
    elif 18.50 <= bmi < 25.00:
        print("標準です。")
    elif 25.00 <= bmi < 30.00:
        print("ふとりぎみです。")
    elif 30.00 <= bmi:
        print("肥満です。")
