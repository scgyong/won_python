import turtle
turtle.speed(0)

def draw_repeated_lines(count, distance, angle, d_inc, a_inc):
    for i in range(count):
        turtle.forward(distance)
        turtle.left(angle)
        distance += d_inc
        angle += a_inc

draw_repeated_lines(10, 10, 0, 20, 5)
draw_repeated_lines(1000, 100, 0, -0.1, -30)

turtle.exitonclick()

