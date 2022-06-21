import tkinter as tk
r=0
c=0

#if __name__=="__main()__":
root = tk.Tk()
root.geometry("300x500")
root.title("電卓")

for num in range(9,-1,-1): 
    button = tk.Button(root, text=f"{num}", width=4, height=2,font=("Times New Roman", 30))
    button.grid(row=r,column=c)
    c+=1
    if (num-1)%3 == 0:
        r+=1
        c=0

root.mainloop()