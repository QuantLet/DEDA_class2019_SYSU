[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **DEDA_class2019_SYSU_Peppa_Pig** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: 'DEDA_class2019_SYSU_Peppa_Pig'
Published in: 'LN_SDA_2019'
Description: 'This Quantlet provides the code to draw PeppaPig by using the library named turtle. 
  The focus lies on the configuration of the pen size, the drawing speed and the fill of the shape.
  The project can be used in stimulate interest of children in python. 
  Reference:https://blog.csdn.net/weixin_33701632/article/details/111928743'
Keywords: 'turtle,  draw, peppa pig, fill, pen, picture, fun'
Author: 'Ruting Rainy WANG' 


```

![Picture1](Peppa%20Pig.png)

### PYTHON Code
```python

# coding:utf-8
import turtle as t
t.pensize(4) # set the pen size 设置画笔的大小
t.colormode(255) #  set the color of GBK 设置GBK颜色范围为0-255
t.color((255,155,192),"pink") # set the pen color(pink) and fill it 设置画笔颜色和填充颜色(pink)
t.setup(840,500) # set the size of main window 设置主窗口的大小为840*500
t.speed(20) # set the speed of drawing 设置画笔速度为10

# draw Peppa Pig's nose
t.pu() # use the pen 提笔
t.goto(-100,100) # go to (-100, 100) 画笔前往坐标(-100,100)
t.pd() # begin to draw 下笔
t.seth(-30) # set the angle of the pen (-30°) 笔的角度为-30°
t.begin_fill() # the signal to fill the figure 外形填充的开始标志
a=0.4 # preset the step length
for i in range(120):
   if 0<=i<30 or 60<=i<90:
       a=a+0.08
       t.lt(3) # turn left 3 degrees向左转3度
       t.fd(a) # go forward step "a" 向前走a的步长
   else:
       a=a-0.08
       t.lt(3)
       t.fd(a)
t.end_fill() # fill the color 依据轮廓填充

# draw Peppa Pig's nostrils
t.pu() # use the pen提笔
t.seth(90) # set the angle of the pen(90°) 笔的角度为90度
t.fd(25) # go forward 25 steps 向前移动25
t.seth(0) # set the angle of the pen(0°)转换画笔的角度为0
t.fd(10)# go forward 10 steps 向前移动10
t.pd()
t.pencolor(255,155,192) # set the pen color(pink) 设置画笔颜色
t.seth(10)
t.begin_fill()
t.circle(5) # Draw a circle with radius 5 画一个半径为5的圆
t.color(160,82,45) # set the pen color(brown)设置画笔和填充颜色
t.end_fill() # fill the figure

# the second nostril
t.pu()
t.seth(0)
t.fd(20)
t.pd()
t.pencolor(255,155,192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()

# draw Peppa Pig's head
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300,-30) #  Draw a circle clockwise with radius of 300 and center anle of 30 顺时针画一个半径为300,圆心角为30°的园
t.circle(100,-60) #  Draw a circle clockwise with radius of 300 and center anle of 60
t.circle(80,-100)
t.circle(150,-20)
t.circle(60,-95)
t.seth(161)  # set the angle of the pen(161°)
t.circle(-300,15)
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)

# repeat 15-25
a=0.4
for i in range(60):
   if 0<=i<30 or 60<=i<90:
       a=a+0.08
       t.lt(3) #向左转3度
       t.fd(a) #向前走a的步长
   else:
       a=a-0.08
       t.lt(3)
       t.fd(a)
t.end_fill()

# Draw Pig's ears
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(-7)
t.seth(0)
t.fd(70)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,54)
t.end_fill()
t.pu()
t.seth(90)
t.fd(-12)
t.seth(0)
t.fd(30)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,56)
t.end_fill()

# Draw Pig's eyes
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-95)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-25)
t.seth(0)
t.fd(40)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()

# Draw Pig's gill
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-95)
t.seth(0)
t.fd(65)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()

# Mouth
t.color(239,69,19)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(-100)
t.pd()
t.seth(-80)
t.circle(30,40)
t.circle(40,80)

# Body
t.color("red",(255,99,71))
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-78)
t.pd()
t.begin_fill()
t.seth(-130)
t.circle(100,10)
t.circle(300,30)
t.seth(0)
t.fd(230)
t.seth(90)
t.circle(300,30)
t.circle(100,3)
t.color((255,155,192),(255,100,100))
t.seth(-135)
t.circle(-80,63)
t.circle(-150,24)
t.end_fill()

# Hands
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-40)
t.seth(0)
t.fd(-27)
t.pd()
t.seth(-160)
t.circle(300,15)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-10)
t.circle(-20,90)
t.pu()
t.seth(90)
t.fd(30)
t.seth(0)
t.fd(237)
t.pd()
t.seth(-20)
t.circle(-300,15)
t.pu()
t.seth(90)
t.fd(20)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-170)
t.circle(20,90)

# Feet
t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(-75)
t.seth(0)
t.fd(-180)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)
t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(40)
t.seth(0)
t.fd(90)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)

# Tail
t.pensize(4)
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(70)
t.seth(0)
t.fd(95)
t.pd()
t.seth(0)
t.circle(70,20)
t.circle(10,330)
t.circle(70,30)

# save 
ts = t.getscreen()
ts.getcanvas().postscript(file="Peppa_Pig.eps")

t.mainloop()

```

automatically created on 2021-01-18