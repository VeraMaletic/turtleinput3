import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')

t=turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write("Background color" ,font=("ariel",30,"normal"),align = "center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write("1. Tan",font=("ariel",20,"normal"),align = "left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('white')
t.write("2. Azure",font=("ariel",20,"normal"),align = "left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('Aquamarine')
t.write("3. Aquamarine",font=("ariel",20,"normal"),align = "left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('DarkKhaki')
t.write("4. DarkKhaki",font=("ariel",20,"normal"),align = "left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write("Choose One",font=("ariel",30,"normal"),align = "Center")

choose = int(input("Choose One: "))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
elif choose == 4:
    screen.bgcolor('darkkhaki')
t.clear()
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('black')
t.write("Enter your name: ",font=("ariel",30,"normal"),align = "center")
name = input("Enter your name: ")
t.clear()
#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter another number: "))
operation = random.randint(1,4 )
if operation == 1:
    #add
    symbol = "+"
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)

    solution = num1 + num2

elif operation == 2:
    # subtract
    symbol = "-"
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)

    solution = num1 - num2

elif operation == 3:
    # multiply
    symbol = "*"
    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 10)

    solution = num1 * num2

elif operation == 4:
        # divide
        symbol = "/"
        num1 = random.randint(-100, 100)
        num2 = random.randint(-100, 100)
        sign = random.randint(1, 2)
        if sign ==2:
            num2= -1*num2



        solution = num1 / num2

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor('red')
t.write(name,font=("ariel",30,"normal"),align = "center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('blue')
t.write(num1,font=("ariel",30,"normal"),align = "center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('purple')
t.write(symbol,font=("ariel",30,"normal"),align = "center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('green')
t.write(num2 ,font=("ariel",30,"normal"),align = "center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('purple')
t.write("=",font=("ariel",30,"normal"),align = "center")

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('black')
t.write(solution,font=("ariel",30,"normal"),align = "center")


answer = float(input("What is the answer: "))

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write("Your answer is: "+str(answer),font=("ariel",30,"normal"),align = "center")

if answer == solution:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("Correct", font=("ariel", 30, "normal"), align="center")
else:
    screen.bgcolor('darkorange')
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor('black')
    t.write("Incorrect", font=("ariel", 30, "normal"), align="center")


