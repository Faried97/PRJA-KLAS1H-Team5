

def setup():
    size(800,600)
    
def draw():
    background(200)
    fill(0)
    
    background(204)
    s = second()  # Values from 0 - 59
    m = minute()  # Values from 0 - 59
    h = hour()  # Values from 0 - 23
    line(s, 0, s, 33)
    line(m, 33, m, 66)
    line(h, 66, h, 100)
    

  

    
    
