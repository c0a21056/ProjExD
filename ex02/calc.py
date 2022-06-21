import tkinter as tk
import tkinter.messagebox as tkm

r=4
c=0
a=4
b=1
d=0

list1 = ["*","-","+","="] #割り算以外の四則演算の計算記号とイコール
list2 = ["%","CE","AC","C","(",")","√","/"] #deleteと()、割り算、％、√

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=": #計算結果の表示
        a = entry.get()
        ans = eval(a)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    elif num =="%": #値を1/100する
        a = entry.get()
        y = eval(a)/100
        entry.delete(0,tk.END)
        entry.insert(tk.END,y)
    elif num =="C": #一文字消す　まだ出来てない
        entry.delete(0,tk.END)
    elif num =="AC": #すべて消す
        entry.delete(0,tk.END)
    else: #数字の表示
        entry.insert(tk.END,f"{num}")

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("電卓")

    for i,num in enumerate([i for i in range(9,0,-1)]  + ["±"] + [0] + ["."]): #電卓の数字部分と ± や . の表示
        button = tk.Button(root, text = f"{num}", width = 3, height = 1, font=("Times New Roman", 30))
        button.grid(row = r, column = c)
        c += 1
        button.bind("<1>", button_click)
        if (i+1)%3 == 0:
            r += 1
            c = 0

    for i,num in enumerate([i for i in list2]): #deleteと()、割り算、％、√の表示
        button = tk.Button(root, text = f"{num}", width = 3, height = 1, font=("Times New Roman", 30))
        button.grid(row = b, column = d)
        d += 1
        button.bind("<1>", button_click)
        if (i+1)%4 == 0:
            b += 1
            d = 0

    for i,num in enumerate([i for i in list1]):#割り算以外の四則演算の計算記号と=の表示
        if i == 4:
            button = tk.Button(root, text = f"{num}", width = 3, height = 1,bg="blue", font=("Times New Roman", 30))
        else:
            button = tk.Button(root, text = f"{num}", width = 3, height = 1, font=("Times New Roman", 30))
        button.grid(row = a, column = 3)
        a += 1
        button.bind("<1>", button_click)

    entry = tk.Entry(root, justify="right", width = 11, font = ("Times New Roman", 40))
    entry.grid(row = 0, columnspan = 5)

    root.mainloop()