import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")#練習3
    kk_img = pg.transform.flip(kk_img, True, False)
    yy_img = pg.image.load("fig/pg_bg.jpg")
    yy_img = pg.transform.flip(yy_img, True, False)
    kk_rct = kk_img.get_rect()#こうかとんrectを取得する
    kk_rct.center = 300, 200#練習10-2
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        yoko=-1
        tate=0
        if key_lst[pg.K_UP]:
            tate=-1
        if key_lst[pg.K_DOWN]:
            tate=1
        if key_lst[pg.K_LEFT]:
            yoko=-2
        if key_lst[pg.K_RIGHT]:
            yoko=1
        
        kk_rct.move_ip((yoko,tate))
        
        x=tmr%3200
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(yy_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()