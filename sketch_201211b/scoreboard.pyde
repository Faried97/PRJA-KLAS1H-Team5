left_score = 0
right_score = 0


def setup():
    size(800,600)

mode = "instruction-screen"

def draw():
    global draw, mode


def draw ():
    background(200)
    if mode == "scoreboard":
        text("x heeft zoveel pionen",300,300)
        
    text("Speler x heeft x pionen", 270,100,)
    textSize(22)
    text(left_score, 40, 40)
    text(right_score, 760, 40)

        
    rectMode(RADIUS) 
    fill(255)  
    rect(400, 300, 150, 150) 

    
