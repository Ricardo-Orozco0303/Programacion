import turtle
import colorsys as cs
import pygame 

def draw_pattern():
    for j in range(25):
        for i in range(25):
            # Obtener valores HSV y ajustarlos para que estén dentro del rango (0, 1)
            hue = i / 25
            saturation = max(0.5, min(1, j / 25))  # Aumentar la saturación para colores más intensos
            value = 0.9  # Aumentar la luminosidad para colores más intensos

            # Utilizar tonalidades asociadas con colores femeninos
            hue = (hue + 0.2) % 1.0  # Desplazar el tono para obtener colores diferentes

            turtle.color(cs.hsv_to_rgb(hue, saturation, value))
            turtle.right(90)
            turtle.circle(200 - j * 4, 90)
            turtle.left(90)
            turtle.circle(200 - j * 4, 90)
            turtle.right(180)
            turtle.circle(50, 24)

def draw_love_message():
    turtle.penup()
    turtle.color("deeppink")  # Utilizar un tono de rosa intenso para el mensaje
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.write("¡Te amo!", align="center", font=("Arial", 16, "normal"))

def main():
    turtle.setup(600, 600)
    turtle.speed(0.100)
    turtle.tracer(10)
    turtle.width(2)
    turtle.bgcolor("black")  # Fondo de negro 

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    draw_pattern()

    draw_love_message()

    turtle.hideturtle()
    turtle.done()
if __name__ == "__main__":
    main()



