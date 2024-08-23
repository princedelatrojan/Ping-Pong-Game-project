#Main Pong Game

#Main importatons
 #Importing the screen of the game
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Describing the screen of the game
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

#Main object for the Game*****
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


#Making the screen to listen for the key strokes
screen.listen()
 #Helping to move the paddle up
screen.onkey(r_paddle.go_up, "Up")
 #Helping to move the paddle Down
screen.onkey(r_paddle.go_down, 'Down')
#The alternating Keys for going up and down
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #To detect if the ball has hit the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #It needs to bounce
        ball.bounce_y()

    #Detection to see if their is contact btwn the paddle and the ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    #Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_postion()
        scoreboard.l_point()

    #To detect left paddle has missed
    if ball.xcor() < -380:
        ball.reset_postion()
        scoreboard.r_point()



screen.exitonclick()