seconds = 0
minutes = 0
hours = 0

def setup ():
    size(250, 500)
   

def draw():
    global seconds
    background(map(second(), 0, 59, 0, 255))
    noStroke()
    fill(map(second(), 80, 59, 255, 0))
    ellipse(width / 2, seconds, 50, 50)
    seconds =+ 1
    if seconds > height:
        seconds = 0
    else:
        seconds = map(second(), 0, 59, 0, height)
    global minutes
    fill(map(minute(), 80, 59, 255, 0))
    ellipse(width / 2, minutes, 50, 50)
    minutes += 1
    if minutes > height:
        minutes = 0
    else:
        minutes = map(minute(), 0, 59, 0, height)
    global hours
    fill(map(hour(), 80, 59, 255, 0))
    ellipse(width / 2, hours, 50, 50)
    hours += 1
    if hours > height:
        hours = 0
    else:
        hours = map(hour(), 0, 59, 0, height)
