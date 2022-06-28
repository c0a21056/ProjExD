import tkinter as tk
import maze_maker

a=["Up","Down","Left","Right"]

def key_down(event):
    global key
    key = event.keysym
    if key in a:
        main_proc()

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy ,mx, my
    cx, cy = mx*100, my*100
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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    #root.geometry("1500x900")
    canvas = tk.Canvas(root, width =1500, height = 900 ,bg = "black")

    maze = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,maze)
    
    tori = tk.PhotoImage(file = "fig/5.png")
    mx,my = 1,1
    cx, cy = mx*150, my*150
    canvas.create_image(cx, cy, image=tori, tag = "tori")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.mainloop()