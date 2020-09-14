from turtle import *
import heart 
from math import atan2, pi, exp
from random import normalvariate



michelangelo = Turtle()
daVinci = Turtle()

michelangelo.color('red', 'blue')
#michelangelo.begin_fill()
#while True:
#    michelangelo.forward(200)
#    michelangelo.left(170)
#    if abs(michelangelo.pos()) < 1:
#        break
#michelangelo.end_fill()


daVinci.color('red', 'yellow')
daVinci.radians()
startpos = daVinci.position()
scale = 1
#daVinci.seth(pi/2)

for t in range(0, round(400*pi)):
    t /= 10
    dpos = [p for p in heart.d_heart(t, h = exp(-15))]
    angle = atan2(dpos[0], dpos[1])-daVinci.heading()+pi
    #angle += normalvariate(0, 0.2)

    if angle > pi:
        angle = angle-pi
    elif angle < -pi:
        angle = angle+2*pi

    if angle < 0:
        daVinci.right(-angle)
    
    else:
        daVinci.left(angle)
    print(angle)

    absdpos = (sum(p**2 for p in dpos))**0.5
    daVinci.forward(absdpos*scale)
    daVinci.pencolor((0.01,1-(10/(t+10)), 0.5))
    scale /= 1.001
    #daVinci.goto(pos)

daVinci.end_fill()
done()