from turtle import*

#drawing a heart
penup()
goto(-100, -10)
pendown()
width(4)
color("hot pink")
begin_fill()
speed(14)
circle(70)
end_fill()

color("hot pink")
begin_fill()
forward(140)
circle(70)
end_fill()


penup()
goto(-150, 10)
color("hot pink")
begin_fill()
right(45)
forward(170)
left(90)
forward(170)
end_fill()

penup()
goto(-30, -20)
pendown()
width(4)
color("hot pink")
begin_fill()
speed(14)
circle(60)
end_fill()
#end of heart






penup()
goto(-60, 20)
pendown()
width(3)
color("purple")
begin_fill()
speed(14)
circle(50)
end_fill()


penup()
goto(70, 20)
pendown()
width(3)
color("pink")
begin_fill()
speed(14)
circle(50)
end_fill()

right(180)
color("beige")
begin_fill()
forward(140)
right(90)
forward(140)
end_fill()


exitonclick()