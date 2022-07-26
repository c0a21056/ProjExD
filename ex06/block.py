import pygame as pg
import sys
import tkinter.messagebox as tkm

class Screen: #Screen
    def __init__(self, title, wh,image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)         
        self.rct = self.sfc.get_rect() 
        self.bgi_sfc = pg.image.load(image)       
        self.bgi_rct = self.bgi_sfc.get_rect()           

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bou: #ボールを反射する棒
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)                       
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()                       
        self.rct.center = xy
    
    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen): #棒の左右移動
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_LEFT] : 
            self.rct.centerx -= 10
        if key_states[pg.K_RIGHT] : 
            self.rct.centerx += 10
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT] :
                self.rct.centerx += 10
            if key_states[pg.K_RIGHT] :
                self.rct.centerx -= 10
        
        self.blit(scr)

    

class Block: #ブロック
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)                
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  
        self.rct = self.sfc.get_rect()                       
        self.rct.center = xy
    
    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr :Screen): 
        self.blit(scr)

class Ball: #ボール
    def __init__(self, color ,size, xy, vxy, ):
        self.sfc = pg.Surface((size*2,size*2)) 
        self.sfc.set_colorkey((0,0,0)) 
        pg.draw.circle(self.sfc, color, (size,size),size)
        self.rct = self.sfc.get_rect() 
        self.rct.center = xy
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr :Screen): #ボールの移動
        self.rct.move_ip(self.vx, self.vy)

        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        self.blit(scr)

    def bound(self): #ボールが棒に当たったら反射する処理
        self.vy *= -1


class Score(): #Score
    def __init__(self, x, y):
        self.sysfont = pg.font.SysFont(None, 20)
        self.score = 0
        (self.x, self.y) = (x, y)

    def draw(self, scr:Screen): #Scoreの表示
        img = self.sysfont.render("SCORE:"+str(self.score), True, (255,255,250))
        scr.sfc.blit(img, (self.x, self.y))

    def add_score(self, x): #Scoreの増加
        self.score += x
    
class Life(): #残機
    def __init__(self, x, y):
        self.sysfont = pg.font.SysFont(None, 20)
        self.life = 3
        (self.x, self.y) = (x, y)

    def draw(self, scr:Screen): #残機の表示
        img = self.sysfont.render("Life:"+str(self.life-1), True, (255,255,250))
        scr.sfc.blit(img, (self.x, self.y))

    def deg_life(self): #残機の減少
        self.life -= 1


def main():
    clock = pg.time.Clock()
    scr = Screen("ブロックを崩せ", (650, 1000),"fig/black.jpg")
    bou = Bou("fig/bou.jpeg",1,(330,900))
    block = None
    ball = Ball((255,0,0), 10, (325,500),(+10, +10))
    score = Score(10, 10)
    life = Life(330,10)

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        bou.update(scr)
        ball.update(scr) 
        score.draw(scr)
        life.draw(scr)

        for i in range(10): #ブロックの描写
            for j in range(10):
                block = Block("fig/01.jpg",1,(50+61*i,50+31*j))
                block.update(scr)

        if bou.rct.colliderect(ball.rct): #ボールが棒に当たったら反射する関数を呼び出す
            ball.bound()

        if ball.rct.colliderect(block.rct): #ボールがブロックに増加したらScoreを増加する関数を呼び出す
            score.add_score(10)

        if ball.rct.bottom > scr.rct.bottom: #床に触れた場合
            life.deg_life()
        if life.life == 0: #残機が0ならゲームオーバー
            return tkm.showinfo("ゲームオーバー", "ゲームオーバーしました")

        key_states = pg.key.get_pressed() 
        if key_states[pg.K_r] : #キー(r)を押したらリスタート
            return main()

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    global life
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()