import random

def main():
    seikai = shutudai()
    kaito(seikai)

def shutudai():
    print("問題：")
    qestion = [{"q":"サザエさんの旦那の名前は？","a":["マスオ","ますお"]},{"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},{"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","甥っこ"]}]
    num = random.randint(0,2)
    print(qestion[num]["q"])
    return qestion[num]["a"]


def kaito(seikai):
    ans = input("答えるんだ")
    if ans in seikai:
         print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()
