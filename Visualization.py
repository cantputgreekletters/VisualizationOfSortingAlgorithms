#imports
import pygame
from random import randint as rn

#Constants

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
GAP = 2
#classes
class Button:
    def __init__(self,text,x=SCREEN_WIDTH/2+50,y=SCREEN_HEIGHT/2):
        color = (255,255,255)
        smallfont = pygame.font.SysFont('Corbel',35)
        self.text = text
        text = smallfont.render(text , True , color)
        SCREEN.blit(text , (x,y))
        self.x,self.y = x,y

    def ButtonRangeX(self):
        Len = 35 * len(self.text) * .5
        return range(int(self.x), int(self.x + Len))
    
    def ButtonRangeY(self):
        return range(int(self.y),int(self.y+35))    
        
class line:
    def __init__(self,x,y) -> None:
        self.x = x
        self.height = y
    
    def draw(self):
        global SCREEN,SCREEN_HEIGHT
        start_pos = pygame.Vector2(self.x,SCREEN_HEIGHT)
        end_pos = pygame.Vector2(self.x,SCREEN_HEIGHT - self.height)
        pygame.draw.line(SCREEN,"orange",start_pos,end_pos)
    
    def __str__(self) -> str:
        start_pos = pygame.Vector2(self.x,SCREEN_HEIGHT)
        end_pos = pygame.Vector2(self.x,SCREEN_HEIGHT - self.height)
        return f'{start_pos} -> {end_pos}'

#functions

def make_lines():
    lines = []
    for x in range(1,SCREEN_WIDTH + 1,GAP):
        lines.append(line(x,rn(1,SCREEN_HEIGHT)))
    return lines

def RenderLines():
    for line in LINES:
        line.draw()

def GetLine(x):
    for line in LINES:
        if x == line.x:
            return line
    raise Exception("Did not return a line")

def Swap(current,other):
    x = current.x
    current.x = other.x
    other.x = x

def SelectionSort():
    current_line = GetLine(idx_start)
    min_line = current_line
    
    for x in range(idx_start + GAP,SCREEN_WIDTH + 1, GAP):
        line = GetLine(x)
        if line.height < min_line.height and line.x > min_line.x:
            min_line = line
    Swap(current_line,min_line)


#Doesnt work
def BubbleSort():
    for x in range(1,SCREEN_WIDTH-idx_start,GAP):
        if x + GAP > SCREEN_WIDTH:
            print("broke")
            break
        print(f'x = {x}')
        CurrentLine = GetLine(x)
        NextLine = GetLine(x + GAP)
        if CurrentLine.height > NextLine.height: 
            Swap(CurrentLine,NextLine)            
            
def mainmenu():
    global algorithm
    while True:
        SCREEN.fill('black')
        MOUSE = pygame.mouse.get_pos()
        Ss = Button('Selection Sort',SCREEN_WIDTH / 2 - 10,SCREEN_HEIGHT / 2 - 50)
        Bs = Button('Bubble Sort',SCREEN_WIDTH / 2 - 10,SCREEN_HEIGHT / 2 + 50)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if MOUSE[0] in Ss.ButtonRangeX() and MOUSE[1] in Ss.ButtonRangeY(): 
                    algorithm = SelectionSort
                    print("entered mainloop")
                    mainloop(SelectionSort)
                elif MOUSE[0] in Bs.ButtonRangeX() and MOUSE[1] in Bs.ButtonRangeY(): 
                    algorithm = BubbleSort
                    print("entered mainloop")
                    mainloop(BubbleSort)

        pygame.display.flip()
        CLOCK.tick(60)

def mainloop(SortingAlgorithm = SelectionSort):
    RUNNING = True
    global idx_start,LINES
    idx_start = 1 - GAP
    LINES = make_lines()
    while RUNNING:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        
        SCREEN.fill("black")
        
        RenderLines()
        if idx_start < SCREEN_WIDTH:
            idx_start += GAP

        if idx_start < SCREEN_WIDTH: 
            print(f"idx_start = {idx_start}")
            SortingAlgorithm()
        
        pygame.display.flip()
        CLOCK.tick(60)



#main
global LINES
pygame.init()
CLOCK = pygame.time.Clock()


mainmenu()

pygame.quit()