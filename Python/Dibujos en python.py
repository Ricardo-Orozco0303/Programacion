import turtle

ventana = turtle.Screen()
mi_tortuga = turtle.Turtle()

# Dibujar el corazón
mi_tortuga.left(50)          # Girar la tortuga a la izquierda en un ángulo de 50 grados

# Dibujar la parte superior del corazón
mi_tortuga.forward(133)      # Mover hacia adelante 133 unidades
mi_tortuga.circle(50, 200)   # Dibujar un arco de círculo con radio 50 y ángulo de 200 grados

# Girar para dibujar la parte inferior del corazón
mi_tortuga.right(140)        # Girar a la derecha en un ángulo de 140 grados
mi_tortuga.circle(50, 200)   # Dibujar otro arco de círculo con las mismas características
mi_tortuga.forward(133)      # Mover hacia adelante para completar la forma del corazón

mi_tortuga.penup()  # Levantar el lápiz para no dejar rastro
mi_tortuga.goto(0, 100)  # Mover la tortuga al centro del cuadrado
mi_tortuga.pendown()  # Bajar el lápiz para empezar a escribir
mi_tortuga.write("¡Te amo!", align="center", font=("Arial", 16, "normal"))
mi_tortuga.hideturtle()
ventana.exitonclick()