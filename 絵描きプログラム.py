import random
import time
import turtle as t
colors = {"red":"あか",
          "yellow":"黄",
          "blue":"青",
          "pink":"ピンク",
          "purple":"紫",
          "gold":"金",
          "silver":"銀",
          "lightblue":"水色",
          "green":"緑",
          "orange":"オレンジ",
          "black":"黒",
          "gray":"グレー"}
t.pensize(5)
t.ht()
t.title("絵描きプログラム")
t.speed(0)
t.tracer(0,0)
def message(m,x,y,s):
    t.teleport(x,y)
    t.color("red")
    t.write(m,align="center",font=("msgothic",s,"bold"))
for _ in range(10):
    line = (random.choice(list(colors.keys())))
    fill = (random.choice(list(colors.keys())))
    t.pencolor(line)
    t.fillcolor(fill)
    t.teleport(-0,-50)

    t.begin_fill()
    x = random.randint(3,18) 
    for _ in range(x):
        t.fd(600/x)
        t.lt(360/x)
    message(f"周りの色は{colors[line]},中の色は{colors[fill]}です",0,-200,20)
    t.end_fill()
    t.update()
    time.sleep(3) 
    t.clear()
t.done()