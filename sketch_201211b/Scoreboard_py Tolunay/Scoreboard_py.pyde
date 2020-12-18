add_library("sound")
player_1 = "Player 1"
player_2 = "Player 2"
score_1 = 0
score_2 = 0
mode = "duel"
def setup():
    fullScreen()
    file = SoundFile(this, "BattleSong.mp3")
    file.play()
    noLoop()
  
def draw():
    global duel, score_1, mode
    background(52, 235, 174)
    fill(235, 52, 113)
    rect(950, 0, 1200,1200)
    textSize(90)
    if score_1 >= 3 or score_2 >= 3:
        mode = "endScreen"
    
    fill(22, 22, 22)
    if mode == 'duel':
        text(player_1 ,320 , 200)
        text(player_2 ,1300 , 200)
        fill(22, 22, 22)
        text(score_1 ,450 , 500)
        text(score_2, 1450 , 500)
        
    elif mode == 'endScreen':
        if score_1 > score_2:
            background(52, 235, 174)
            text('PLAYER 1 HAS WON THE BATTLE' ,350 , 500)
        else:
            background(235, 52, 113)
            text('PLAYER 2 HAS WON THE BATTLE' ,350 , 500)
    
    
def mousePressed():
    global score_1, score_2
    if mouseX <= 950 and mouseY <= 1200:
        score_1 += 1
        
    elif mouseX >= 951 and mouseY <= 1200:
        score_2 += 1
        
    redraw()
