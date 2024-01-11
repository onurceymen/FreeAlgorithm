import random
import turtle
import time
delay = 0.15

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor('red')
window.setup(width=600, height=600, startx=500, starty=500)
window.tracer(0)

snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("black")
snakeHead.penup()
snakeHead.goto(0,100)
snakeHead.direction = "stop"

bait = turtle.Turtle()
bait.speed(0)
bait.shape("circle")
bait.color("white")
bait.penup()
bait.shapesize(0.80, 0.80)
bait.goto(0,0)

Tails = []
point = 0

write = turtle.Turtle()
write.speed(0)
write.shape("square")
write.color("white")
write.penup()
write.hideturtle()
write.goto(0,260)
write.write("Puan: {}".format(point), align="center", font=("Courier", 24, "normal"))

def move():
    if snakeHead.direction == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y + 20)
    elif snakeHead.direction == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y - 20)  # Corrected to y - 10 for "down"
    elif snakeHead.direction == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x + 20)
    elif snakeHead.direction == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x - 20)  # Corrected to x - 10 for "left"

def go_up():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
def go_down():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"
def go_right():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"
def go_left():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")
while True:
    window.update()
    if snakeHead.xcor() > 300 or snakeHead.xcor() < -300 or snakeHead.ycor() > 300 or snakeHead.ycor() < -300:
        time.sleep(1)
        snakeHead.goto(0, 0)
        snakeHead.direction = "stop"

        for Tail in Tails:
            Tail.goto(1000, 1000)

        point = 0
        delay = 0.1

        write.clear()
        write.write("Puan: {}".format(point), align="center", font=("Courier", 24, "normal"))

    if snakeHead.distance(bait) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        bait.goto(x, y)

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("white")
        new_tail.penup()
        Tails.append(new_tail)

        delay -= 0.001

        point = point + 10
        write.clear()
        write.write("Puan: {}".format(point), align="center", font=("Courier", 24, "normal"))

    for index in range(len(Tails) - 1, 0, -1):
        x = Tails[index - 1].xcor()
        y = Tails[index - 1].ycor()
        Tails[index].goto(x, y)

    if len(Tails) > 0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        Tails[0].goto(x, y)

    move()

    for segment in Tails:
        if segment.distance(snakeHead) < 20:
            time.sleep(1)
            snakeHead.goto(0, 0)
            snakeHead.direction = "stop"
            for segment in Tails:
                segment.goto(1000, 1000)
            Tails = []
            point = 0
            write.clear()
            write.write('Puan: {}'.format(point), align='center', font=('Courier', 24, 'normal'))
            speed = 0.15

    time.sleep(delay)
































