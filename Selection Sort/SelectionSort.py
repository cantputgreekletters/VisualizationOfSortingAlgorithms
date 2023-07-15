#imports
import pygame
from random import randint as rn
from time import sleep
#Constants

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
idx_start = -1
#classes
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
    for x in range(1,SCREEN_WIDTH + 1,2):
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

def SortLines():
    print(idx_start)
    current_line = GetLine(idx_start)
    min_line = current_line
    print(f"first curret line {current_line}")
    for x in range(idx_start + 2,SCREEN_WIDTH + 1, 2):
        line = GetLine(x)
        if line.height < min_line.height and line.x > min_line.x:
            min_line = line
    x = current_line.x
    current_line.x = min_line.x
    min_line.x = x
    print(f'new current line {current_line}')

def mainloop():
    global RUNNING,idx_start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    
    SCREEN.fill("black")
    
    RenderLines()
    if idx_start < SCREEN_WIDTH:
        idx_start += 2

    if idx_start < SCREEN_WIDTH: 
        
        SortLines()
    pygame.display.flip()
    CLOCK.tick(60)
#main
pygame.init()
CLOCK = pygame.time.Clock()
RUNNING = True
LINES = make_lines()
while RUNNING: mainloop()
pygame.quit()