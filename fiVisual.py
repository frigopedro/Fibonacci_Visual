import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")

# catetos
linha = turtle.Turtle()
linha.color("grey")
linha.hideturtle()
linha.speed(0)
linha.left(90)
linha.forward(1000)
linha.goto(0,0)
linha.left(90)
linha.forward(1000)
linha.goto(0,0)
linha.left(90)
linha.forward(1000)
linha.goto(0,0)
linha.left(90)
linha.forward(1000)

for c in range(0, 20):
    linha.goto(0, 10)
    linha.dot(10, "white")
    


# circulo

bola = turtle.Turtle()
bola.color("white")
bola.hideturtle()


# fibonacci
contador = 0
fibonacci = [0, 1]

for c in range(0, 20):
    contador += 1
    soma = fibonacci[contador - 1] + fibonacci[contador]
    fibonacci.append(soma)
contador = 0
for ce in range (0, 20):
    contador += 1
    term = fibonacci[contador - 1]
    bola.circle(term, 90)
