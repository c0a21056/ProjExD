import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #1600x900の画面surfaceを生成
    screem_rect = screen_sfc.get_rect() #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bgimg_rect = bgimg_sfc.get_rect() #Rect
    #screen_sfc.blit(bgimg_sfc,bgimg_rect)

    tori_img = pg.image.load("fig/6.png") #Surface
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()  #Rect
    tori_rect.center = 900, 400
    #screen_sfc.blit(tori_img, tori_rect) #screen Surfaceにtori_img Surfaceをtori_rectにしたがって貼り付ける

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rect)
        screen_sfc.blit(tori_img, tori_rect) 
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        pg.display.update()
        clock.tick(1000) 

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()