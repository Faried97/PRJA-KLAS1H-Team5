from random import randint


class flake:
    def __init__ (self,x,y):
        self.vec = PVector(x,y)        
        self.z = random(0,3)
        self.velY = map(self.z,0,3,0.5,1)
        self.velX = 0
        
    def show(self):
        ellipse(self.vec.x,self.vec.y,map(self.z,0,3,2,5),map(self.z,0,3,2,5))
        
    def update(self):
        self.vec.y += self.velY
        self.vec.x += self.velX
        self.velY += 0.01 
        if self.velX > 0:
            self.velX -= 0.01
        elif self.velX < 0:
            self.velX += 0.01
        
        if self.vec.y > height:
            self.vec.x = randint(0,width)
            self.vec.y = randint(-500,-50)
            self.velY = map(self.z,0,3,0.5,1.5)
        if self.vec.x < 0: 
            self.vec.x = randint(350,width)
        if self.vec.x > width: 
            self.vec.x = randint(0,100)
            
        

width = 2000
height = 6800
snow = []
total = 5001 #num of snowflakes

for i in range(0,total):
    snow.append(flake(randint(0,width),randint(-500,50)))
    
    
def setup():
    fullScreen()
    noStroke()

string1 = ''
string2 = ''
string3 = ''
string4 = ''
def draw(): # het programma heeft draw() nodig zodat het kan runnen.
    
    background(67, 67, 67)
    for i in range(0,total):
        snow[i].show()
        snow[i].update()
        


    #vorm van het invoer veld    
    fill(0, 100, 0)
    rect(430, 320, 655, 55, 7)
    #invoer veld
    fill(255,250,250)
    textSize(26)
    text(string1, 460,355)
    
    #vorm van het invoer veld    
    fill(255, 0, 0)
    rect(430, 420, 655, 55, 7)
    #invoer veld
    fill(255,250,250)
    textSize(26);
    text(string2, 460,455)
    
    #vorm van het invoer veld    
    fill(153,153,0)
    rect(430, 520, 655, 55, 7)
    #invoer veld
    fill(255,250,250)
    textSize(26);
    text(string3, 460,555)
    
    #vorm van het invoer veld    
    fill(65,105,225)
    rect(430, 620, 655, 55, 7)
    #invoer veld
    fill(255,250,250)
    textSize(26);
    text(string4, 460,655)
    
    #button
    rect(640, 720, 240, 55, 7)
    textSize(26)
    fill(12,12,12)
    text('ENTER THE GAME', 650, 755)
    
    textSize(66)
    fill(225, 145, 45)
    text('Welkom', 850, 100, 4)
    fill(255,222,173)
    textSize(45)
    text('Kies een kleur en vul je naam in', 430, 250, 4)
    fill(255,250,250)

def keyTyped():
    global string1, string2, string3, string4
    
    string1 = string1 + key # "key" is de ingedrukte toets.
    print('string: ' + string1)
    print('toets: ' + key)
    
    if key == ENTER:
        string2 = string2 + key # "key" is de ingedrukte toets.
        print('string: ' + string2)
        print('toets: ' + key)
    
    string3 = string3 + key # "key" is de ingedrukte toets.
    print('string: ' + string3)
    print('toets: ' + key)

    string4 = string4 + key # "key" is de ingedrukte toets.
    print('string: ' + string4)
    print('toets: ' + key)

# def mouseClicked():
#     global string1
#     if string1 == True:
    
