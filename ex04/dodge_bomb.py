import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

i=0
c=0
a=0

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #1600x900の画面surfaceを生成
    screen_rect = screen_sfc.get_rect() #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bgimg_rect = bgimg_sfc.get_rect() #Rect
    screen_sfc.blit(bgimg_sfc,bgimg_rect)

    b = random.randint(0,9)
    tori_sfc = pg.image.load(f"fig/{b}.png") #Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rect = tori_sfc.get_rect() #Rect
    tori_rect.center = 900, 400

    bomb_sfc = pg.Surface((20,20)) #Surface
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255,0,0),(10,10),10)
    bomb_rect = bomb_sfc.get_rect() #Rect
    bomb_rect.centerx = random.randint(0,screen_rect.width)
    bomb_rect.centery = random.randint(0,screen_rect.height)
    vx,vy = +1,+1

    
    while True:
        global i,c,a

        screen_sfc.blit(bgimg_sfc,bgimg_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT: return #xを押した場合の処理

        key_lit = pg.key.get_pressed() #こうかとんの移動
        if key_lit[pg.K_UP] == True: tori_rect.centery -=1
        if key_lit[pg.K_DOWN] == True: tori_rect.centery +=1
        if key_lit[pg.K_LEFT] == True: tori_rect.centerx -=1
        if key_lit[pg.K_RIGHT] == True: tori_rect.centerx +=1

        if check_bound(tori_rect, screen_rect) != (1,1):
            if key_lit[pg.K_UP] == True: tori_rect.centery +=1
            if key_lit[pg.K_DOWN] == True: tori_rect.centery -=1
            if key_lit[pg.K_LEFT] == True: tori_rect.centerx +=1
            if key_lit[pg.K_RIGHT] == True: tori_rect.centerx -=1

        if tori_rect.colliderect(bomb_rect) == True:
            x =  tori_rect.centerx
            y =  tori_rect.centery
            b = random.randint(0,9)
            tori_sfc = pg.image.load(f"fig/{b}.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
            tori_rect = tori_sfc.get_rect()
            tori_rect.center =  x,y
            vx *= -1
            vy *= -1
            i += 1
        
        if i >= 3:
            tkm.showinfo("ゲームオーバー", "ゲームオーバーです")
            return pg.QUIT
        
        if key_lit[pg.K_u] == True:
            vx *=1.02
            vy *=1.02

        if key_lit[pg.K_b] == True:
            x =  bomb_rect.centerx
            y =  bomb_rect.centery
            a+=0.5
            bomb_sfc = pg.Surface((20+a,20+a)) #Surface
            bomb_sfc.set_colorkey((0,0,0))
            pg.draw.circle(bomb_sfc, (255,0,0),(10+a/2,10+a/2),10+a/2)
            bomb_rect = bomb_sfc.get_rect() #Rect
            bomb_rect.centerx = x
            bomb_rect.centery = y


        if key_lit[pg.K_s] == True:
            x =  bomb_rect.centerx
            y =  bomb_rect.centery
            a-=0.5
            bomb_sfc = pg.Surface((20+a,20+a)) #Surface
            bomb_sfc.set_colorkey((0,0,0))
            pg.draw.circle(bomb_sfc, (255,0,0),(10+a/2,10+a/2),10+a/2)
            bomb_rect = bomb_sfc.get_rect() #Rect
            bomb_rect.centerx = x
            bomb_rect.centery = y

        screen_sfc.blit(tori_sfc, tori_rect) 

        bomb_rect.move_ip(vx,vy)
        
        screen_sfc.blit(bomb_sfc, bomb_rect)

        yoko,tate =  check_bound(bomb_rect, screen_rect)
        vx *= yoko 
        vy *= tate 

        pg.display.update()
        clock.tick(1000) 

def check_bound(rect, scr_rect):
    yoko,tate = +1,+1
    if rect.left < scr_rect.left or rect.right > scr_rect.right: yoko = -1
    if rect.top < scr_rect.top or rect.bottom > scr_rect.bottom: tate = -1
    return yoko,tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()