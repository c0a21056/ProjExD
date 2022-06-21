import tkinter as tk
import tkinter.messagebox as tkm

r=1
c=0

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo(num, f"[{num}]ボタンが押されました")
    entry.insert(tk.END,f"{num}")

#if __name__=="__main()__":
root = tk.Tk()
#root.geometry("300x500")
root.title("電卓")

for num in range(9,-1,-1): 
    button = tk.Button(root, text=f"{num}", width=4, height=2,font=("Times New Roman", 30))
    button.grid(row=r,column=c)
    c+=1
    button.bind("<1>",button_click)
    if (num-1)%3 == 0:
        r+=1
        c=0

entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman", 40))
entry.grid(row=0,columnspan=3)

root.mainloop()