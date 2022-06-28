import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
import random 

move=["Up","Down","Left","Right"] #矢印のリスト

def key_down(event):
    global key
    key = event.keysym
    if key in move: #入力されたキーが矢印かを判別し矢印ならmain_proc関数を実行する
        main_proc()

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy ,mx, my, b, tori
    b = random.randint(0,9) #こうかとんの画像を選ぶ数の設定
    tori = tk.PhotoImage(file = f"fig/{b}.png") #こうかとんの画像の変更
    if key == "Up" and maze[my-1][mx] == 0 :
        my -= 1
    elif key == "Down" and maze[my+1][mx] == 0:
        my += 1
    elif key == "Left" and maze[my][mx-1] == 0:
        mx -= 1
    elif key == "Right" and maze[my][mx+1] == 0:
        mx += 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)
    canvas.create_image(cx, cy, image=tori, tag = "tori")
    if cx == 1350:
        if cy == 750:
            tkm.showinfo("ゴール", "ゴールにつきました")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    #root.geometry("1500x900")
    canvas = tk.Canvas(root, width =1500, height = 900 ,bg = "black")

    maze = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,maze)
    
    b = random.randint(0,9)
    tori = tk.PhotoImage(file = f"fig/{b}.png")
    mx,my = 1,1
    cx, cy = mx*150, my*150
    canvas.create_rectangle(100, 100, 200, 200,fill="blue")
    canvas.create_rectangle(1300, 700, 1400, 800,fill="red")
    canvas.create_image(cx, cy, image=tori, tag = "tori")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()