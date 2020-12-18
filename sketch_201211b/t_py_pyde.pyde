import time

def setup():
    size(700,500)
    frameRate(60)
    


def draw_time():
    t = int(input("How many seconds do you want to set the timer for? "))
    background(100)
    fill(100)
    text(t,50,50)
    while t:
        mins = t//60
        secs = t% 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
def setup():
    size(700,500)

def draw():
    pass

        
def mousePressed():
    if(mouseButton == LEFT):
        start.timer()
    elif(mouseButton == RIGHT):
        stop.timer()
        
