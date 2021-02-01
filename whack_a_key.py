#Whack a key
import pygame,random,sys
pygame.init()

w=800
h=600
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Whack a key')

keys={'a':False,'b':False,'c':False,'d':False,'e':False,'f':False,'g':False,'h':False,'i':False,'j':False,'k':False,'l':False,'m':False,'n':False,'o':False,'p':False,'q':False,'r':False,'s':False,'t':False,'u':False,'v':False,'w':False,'x':False,'y':False,'z':False,'\\':False}
curkey=random.choice(list(keys))
keys[curkey]=True
score=0
deftime=1000
time=deftime

back=pygame.image.load('Backspace.png')
back=pygame.transform.scale(back,(60,40))
backrect=back.get_rect()
backrect.center=(463,305)

def win():
    global score,keys,curkey,time,deftime
    print(deftime)
    if time>=0:
        score+=1
        deftime-=5
    else:#...
        pass
    for i in keys:
        keys[i]=False
    curkey=random.choice(list(keys))
    keys[curkey]=True
    if deftime<100:
        deftime=100
    time=deftime

font=pygame.font.SysFont('comicsansms',35)
BIGfont=pygame.font.SysFont('comicsansms',45)

keytext=BIGfont.render(curkey,True,(255,0,204))
scoretext=font.render(str(score),True,(255,0,204))
name=font.render('Whack a key',True,(255,0,204))

keyrect=keytext.get_rect(center=(w//2,h//2))
scorerect=scoretext.get_rect(topleft=(20,-20))
namerect=name.get_rect(topright=(w-20,20))

while True:
    pygame.time.wait(1)
    time-=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type==pygame.KEYDOWN:
            if keys['q']:
                if event.key==pygame.K_q:
                    win()
            elif keys['w']:
                if event.key==pygame.K_w:
                    win()
            elif keys['e']:
                if event.key==pygame.K_e:
                    win()
            elif keys['r']:
                if event.key==pygame.K_r:
                    win()
            elif keys['t']:
                if event.key==pygame.K_t:
                    win()
            elif keys['y']:
                if event.key==pygame.K_y:
                    win()
            elif keys['u']:
                if event.key==pygame.K_u:
                    win()
            elif keys['i']:
                if event.key==pygame.K_i:
                    win()
            elif keys['o']:
                if event.key==pygame.K_o:
                    win()
            elif keys['p']:
                if event.key==pygame.K_p:
                    win()
            elif keys['a']:
                if event.key==pygame.K_a:
                    win()
            elif keys['s']:
                if event.key==pygame.K_s:
                    win()
            elif keys['d']:
                if event.key==pygame.K_d:
                    win()
            elif keys['f']:
                if event.key==pygame.K_f:
                    win()
            elif keys['g']:
                if event.key==pygame.K_g:
                    win()
            elif keys['h']:
                if event.key==pygame.K_h:
                    win()
            elif keys['j']:
                if event.key==pygame.K_j:
                    win()
            elif keys['k']:
                if event.key==pygame.K_k:
                    win()
            elif keys['l']:
                if event.key==pygame.K_l:
                    win()
            elif keys['z']:
                if event.key==pygame.K_z:
                    win()
            elif keys['x']:
                if event.key==pygame.K_x:
                    win()
            elif keys['c']:
                if event.key==pygame.K_c:
                    win()
            elif keys['v']:
                if event.key==pygame.K_v:
                    win()
            elif keys['b']:
                if event.key==pygame.K_b:
                    win()
            elif keys['n']:
                if event.key==pygame.K_n:
                    win()
            elif keys['m']:
                if event.key==pygame.K_m:
                    win()
            elif keys['\\']:
                if event.key==pygame.K_BACKSLASH:
                    win()
            
    if time<0:
        win()
    
    screen.fill((0,0,0))
    
    keytext=BIGfont.render(curkey,True,(255,0,204))
    scoretext=font.render(str(score),True,(255,0,204))
    name=font.render('Whack a key',True,(255,0,204))

    keyrect=keytext.get_rect(center=(w//2,h//2))
    scorerect=scoretext.get_rect(topleft=(20,20))
    namerect=name.get_rect(topright=(w-20,20))
    
    screen.blit(keytext,keyrect)
    screen.blit(scoretext,scorerect)
    screen.blit(name,namerect)
    screen.blit(back,backrect)
                    
                    
    pygame.display.update()