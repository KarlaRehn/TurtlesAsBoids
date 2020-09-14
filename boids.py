#boids 

from turtle import *
from random import normalvariate, randint
from typing import Sequence, Tuple

class Flock():
    flock = [] # type: Sequence[Turtle]

    def __init__(self, antal_boids: int):
        for _ in range(antal_boids):
            nyturtle = Turtle()
            nyturtle.penup()
            x = normalvariate(0, 100)
            y = normalvariate(0, 100)
            nyturtle.setposition(x, y)
            nyturtle.setheading(randint(0, 360))
            self.flock.append(nyturtle)

    def flyga(self):
        mp = self.mittpunkt()
        for boid in self.flock:
            angle = boid.towards(mp)
            boid.left(angle-boid.heading())
            angle = randint(-100, 100)
            boid.left(angle)
            boid.forward(10)
            closest = min((b for b in self.flock if b != boid), key=lambda b: boid.distance(b))
            '''if boid.distance(closest) < 20:
                krockvinkel1 = boid.towards(closest)
                krockvinkel2 = closest.heading()
                boid.left(krockvinkel + 30)'''

            
    
    def mittpunkt(self) -> Tuple[int, int]:
        x = 0
        y = 0
        for boid in self.flock:
            x += boid.xcor()
            y += boid.ycor()
        return (x/len(self.flock), y/len(self.flock))

        

window = Screen()
window.delay(0)

window.bgcolor((0.1, 0.4, 0.8))
flock = Flock(10)
while True:
    flock.flyga()
done()