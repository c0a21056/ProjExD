import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)         # Surface
        self.rct = self.sfc.get_rect()             # Rect
        self.bgi_sfc = pg.image.load(image)        # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()     # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)                      # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()                       # Rect
        self.rct.center = xy
    
    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] : 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN] : 
            self.rct.centery += 1
        if key_states[pg.K_LEFT] : 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT] : 
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP] : 
                self.rct.centery += 1
            if key_states[pg.K_DOWN] :
                self.rct.centery -= 1
            if key_states[pg.K_LEFT] :
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT] :
                self.rct.centerx -= 1
        
        self.blit(scr)


class Bomb:
    def __init__(self, color ,size, vxy, scr: Screen):
        self.sfc = pg.Surface((size*2,size*2)) # Surface
        self.sfc.set_colorkey((0,0,0)) 
        pg.draw.circle(self.sfc, color, (size,size),size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr :Screen):
        self.rct.move_ip(self.vx, self.vy)

        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        self.blit(scr)

class Enemy:
    def __init__(self, image: str, size: float, xy ,scr: Screen):
        self.sfc = pg.image.load(image)                      # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = xy                       
    
    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    
    def update(self, scr :Screen):
        self.rct.move_ip(self.vx, self.vy)

        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        self.blit(scr)


class Beam:
    def __init__(self, image: str, size: float, x, y, vx, scr:Screen ):
        self.sfc = pg.image.load(image)                      # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()                       # Rect
        self.rct.centerx = x
        self.rct.centery = y
        self.vx, self.vy = vx

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy) 

        self.blit(scr)


def main():
    clock = pg.time.Clock()

    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    tori = Bird("fig/6.png",2.0,(900, 400))

    bomb = Bomb((255,0,0), 10, (+1, +1), scr)

    enemy = Enemy("fig/a.png",0.5, (+1,+1) ,scr)

    beam = Beam("fig/beam.png",0.05, tori.rct.centerx,tori.rct.centery, (+1,+0) ,scr)

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tori.update(scr)

        bomb.update(scr)

        enemy.update(scr)

        key_states = pg.key.get_pressed()
        if key_states[pg.K_SPACE] :
            beam.update(scr)

        if beam.rct.colliderect(enemy.rct):
            tkm.showinfo("ゲームクリア", "ゲームクリアです")
            return

        if tori.rct.colliderect(bomb.rct):
            tkm.showinfo("ゲームオーバー", "ゲームオーバーです")
            return
        
        if tori.rct.colliderect(enemy.rct):
            tkm.showinfo("ゲームオーバー", "ゲームオーバーです")
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()