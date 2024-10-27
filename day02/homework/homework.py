from turtle import*

#draw a palace
penup()
goto(-250, -250)
pendown()
color("beige")
begin_fill()
speed(9)
forward(460)
left(90)
forward(300)
left(45)
forward(150)
left(45)
forward(250)
left(45)
forward(150)
left(45)
forward(300)
end_fill()

#end of main shape

#draw the door 
left(90)
forward(150)
color("violet")
begin_fill()
left(90)
forward(200)
right(45)
forward(110)
right(90)
forward(110)
right(45)
forward(200)
end_fill()

#end of the door

#drawing the roof
penup()
goto(106, 156)
pendown()
color("hot pink")
begin_fill()
left(130)
forward(75)
left(100)
forward(240)
left(80)
forward(240)
left(100)
forward(75)
end_fill()

#end of the roof

#draw the left window 
penup()
goto(-220, -70)
pendown()
color("pink")
begin_fill()
left(40)
forward(90)
left(90)
forward(90)
left(90)
forward(90)
left(90)
forward(90)
end_fill()
#end of the left window


#draw the right window
penup()
goto(80, 20)
pendown()
color("purple")
begin_fill()
forward(90)
left(90)
forward(90)
left(90)
forward(90)
left(90)
forward(90)
left(90)
end_fill()
#end of the right window

#end of a palace

exitonclick()