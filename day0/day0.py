from turtle import *

#home

width (6)
forward (250)
left (90)
speed (30)
color
begin_fill()

forward(300)
left(90) 
forward(260)
left(90)
forward(300)

#door

left(90)
forward (60)
left(90)
forward(140)
right(90)
forward(70)
right(90)
forward(140)

#roof

penup()
goto (250, 300)
pendown()

color("pink")
begin_fill()
right(150)
forward (250)
left(117)
forward(254)
end_fill()

#window

color ("black")
penup()
goto(140, 120)
pendown()

left (34)
forward (50)
left(90)
forward (50)
left(90)
forward (50)
left(90)
forward (50)

# secondfloor

penup()
goto(-11, 150)
pendown()

left (180)
forward (265)
         
penup()
goto (5,270)
pendown ()

forward (70)
right(90)
forward (70)
right(90)
forward (70)
right(90)
forward (70)
right(90)

penup()
goto(160, 270)
pendown()

forward (70)
right(90)
forward (70)
right(90)
forward (70)
right(90)
forward (70)
right(90)



exitonclick()