import turtle
import time
import random

delay = 0.1
body_segments = []
score = 0
high_score = 0

windows = turtle.Screen()
#Title
windows.title("Snake Game")
#Windows size
windows.setup(width=600, height=600)
#Background color
windows.bgcolor("light green")

#Head settings
#Turtle obj
head = turtle.Turtle()
#Fixed point
head.speed(0)
#shape
head.shape("square")
#head color
head.color("green")
#clean the animation
head.penup()
#center
head.goto(0, 0)

#waiting for a direction order
head.direction = "Stop"

#food config
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red")
food.penup()
food.goto(0,100)
food.direction = "stop"

#Score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write(f"Score 0      High Score 0", align="center", font=("Arial",24))


def mov():
    if head.direction == "up":
        #almacenar el valor de la coor Y:
        y = head.ycor()
        head.sety(y + 10)
        
    if head.direction == "down":
        #almacenar el valor de la coor Y:
        y = head.ycor()
        #almacenar el valor de la coor X:
        x = head.xcor()
        head.sety(y - 10)

    if head.direction == "right":
        #almacenar el valor de la coor Y:
        y = head.xcor()
        head.setx(y + 10)

    if head.direction == "left":
        #almacenar el valor de la coor Y:
        y = head.xcor()
        head.setx(y - 10)

def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"

#connect keyboard
windows.listen()
windows.onkeypress(dirUp, "Up")
windows.onkeypress(dirDown, "Down")
windows.onkeypress(dirRight, "Right")
windows.onkeypress(dirLeft, "Left")

                  
while True:
    windows.update()
    
     #Head vs Windows
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

       #hide

        for segment in body_segments:
            segment.goto(1000, 1000)
       #clean
        body_segments.clear()
        score = 0
        text.clear()
        text.write(f"Score {score}      High Score {high_score}", align="center", font=("Arial",24))


       #head vs food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)   
    #New segment config
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        body_segments.append(new_segment)

        score += 1
        if score > high_score:
            high_score = score

        text.clear()
        text.write(f"Score {score}      High Score {high_score}", align="center", font=("Arial",24))

    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)
                       
    mov()

     #eat myself
    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in body_segments:
                segment.goto(1000, 1000)

            body_segments.clear()
            score = 0
            text.clear()
            text.write(f"Score {score}      High Score {high_score}", align="center", font=("Arial",24))

    time.sleep(delay)

turtle.done()
