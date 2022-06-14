import random
import datetime
from this import d

t = 10  #対象文字数
k = 2  #欠損文字数
m = [] #取り出した文字を入れるList

def main():
    st = datetime.datetime.now()
    a()
    num()
    ed = datetime.datetime.now()
    print((ed-st).seconds)

def a():
    alp = [chr(c+65) for c in range(26)]
    a = random.sample(alp,t)
    print("対象文字：")
    print(a)
    for i in range(k):
        miss = random.randint(0,9)
        m.append(a.pop(miss))
    print("表示文字：")
    print(a)

def num():
    ans = int(input("欠損文字数はいくつあるでしょうか？："))
    if ans == int(k):
         print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
         seikai()
    else:
        print("違いますもう一度入力してください")
        num()

def seikai():
    sei = input("一つ目の文字を入力してください:")
    if sei in m:
        sei2 = input("二つ目の文字を入力してください:")
        if sei2 in m:
            print("正解です。ありがとうございました")
        else:
            print("不正解です。またチャレンジしてください")
            m.clear()
            main()
    else:
        print("不正解です。またチャレンジしてください")
        m.clear()
        main()

if __name__ == "__main__":
    main()