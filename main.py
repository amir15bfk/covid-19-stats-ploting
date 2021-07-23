import pygame,sys
from pygame.locals import *
from api import *
from ploting import Plot

pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE = 1
BG_COLOR=pygame.Color(255,255,255)
class Game_env:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH*SCALE,SCREEN_HEIGHT*SCALE))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('covid 19 stats')
        #load images
        self.total_recovered_bg_img = pygame.image.load('img/total recovered.png').convert_alpha()
        self.total_cases_bg_img = pygame.image.load('img/total cases.png').convert_alpha()
        self.total_deaths_bg_img = pygame.image.load('img/total deaths.png').convert_alpha()
        self.new_recovered_bg_img = pygame.image.load('img/new recovered.png').convert_alpha()
        self.new_cases_bg_img = pygame.image.load('img/new cases.png').convert_alpha()
        self.new_deaths_bg_img = pygame.image.load('img/new deaths.png').convert_alpha()

        self.new_cases_img = pygame.image.load('img/new cases b.png').convert_alpha()
        self.new_deaths_img = pygame.image.load('img/new deaths b.png').convert_alpha()
        self.new_recovered_img = pygame.image.load('img/new recovered b.png').convert_alpha()
        self.total_cases_img = pygame.image.load('img/total cases b.png').convert_alpha()
        self.total_deaths_img = pygame.image.load('img/total deaths b.png').convert_alpha()
        self.total_recovered_img = pygame.image.load('img/total recovered b.png').convert_alpha()

        space = 14
        self.new_cases_button = Button(self.new_cases_img,20,20,191,96)
        self.new_deaths_button = Button(self.new_deaths_img,20,20+space+96,191,96)
        self.new_recovered_button = Button(self.new_recovered_img,20,20+space*2+96*2,191,96)
        self.total_cases_button = Button(self.total_cases_img,20,20+space*3+96*3,191,96)
        self.total_deaths_button = Button(self.total_deaths_img,20,20+space*4+96*4,191,96)
        self.total_recovered_button = Button(self.total_recovered_img,20,20+space*5+96*5,191,96)

        self.bg_button = Button(self.total_cases_bg_img,0,0,0,0)
        # self.map_button.rect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        data = get_total_cases()
        self.plot = Plot(453,600,data)

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.bg_button.draw(self.screen)
        self.new_cases_button.draw(self.screen)
        self.new_deaths_button.draw(self.screen)
        self.new_recovered_button.draw(self.screen)
        self.total_cases_button.draw(self.screen)
        self.total_deaths_button.draw(self.screen)
        self.total_recovered_button.draw(self.screen)
        self.plot.plot(self.screen)

    def loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button==1:
                        mx,my=pygame.mouse.get_pos()
                        if self.new_cases_button.rect.collidepoint((mx,my)):
                            self.bg_button.set_img(self.new_cases_bg_img)
                            self.plot.set_data(get_new_cases())
                        elif self.new_deaths_button.rect.collidepoint((mx,my)):
                            self.bg_button.set_img(self.new_deaths_bg_img)
                            self.plot.set_data(get_new_deaths())
                        elif self.new_recovered_button.rect.collidepoint((mx,my)):
                            self.bg_button.set_img(self.new_recovered_bg_img)
                            self.plot.set_data(get_new_recovered_cases())
                        elif self.total_cases_button.rect.collidepoint((mx,my)):
                            self.bg_button.set_img(self.total_cases_bg_img)
                            self.plot.set_data(get_total_cases())
                        elif self.total_deaths_button.rect.collidepoint((mx,my)):
                            self.bg_button.set_img(self.total_deaths_bg_img)
                            self.plot.set_data(get_total_deaths())
                        elif self.total_recovered_button.rect.collidepoint((mx,my)):
                            self.bg_button.set_img(self.total_recovered_bg_img)
                            self.plot.set_data(get_total_recovered_cases())
            self.draw()  
            pygame.display.flip()
            self.clock.tick(60)
class Button():
    def __init__(self,img,x,y,width,height,scale=1):
        self.img =img
        if width:
            self.img=pygame.transform.scale(img, (width, height))
        self.rect = self.img.get_rect()
        self.rect.topleft=(x,y)
    
    def draw(self,screen):
        screen.blit(self.img,(self.rect.x,self.rect.y))
    
    def set_img(self,img):
        self.img = img
game =Game_env()
game.loop()