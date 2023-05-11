from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

segments = []

def handle_food(snake, food, scoreboard):
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_to_score()
        snake.extend_snake()


def did_collide_edge(head):
    edge = 295
    end_x_cor = head.xcor() > edge or head.xcor() < - edge
    end_y_cor = head.ycor() > edge or head.ycor() < - edge

    if end_x_cor or end_y_cor:
        return True

    return False


def did_collide_self(snake):
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True

    return False

def run():
    game_is_on = True
    snake = Snake(screen)
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move_segments()

        # detect if caught food
        handle_food(snake, food, scoreboard)

        # detect collision with edge or tail
        if did_collide_edge(snake.head) or did_collide_self(snake):
            game_is_on = False
            scoreboard.write_score(True)

run()

screen.exitonclick()
