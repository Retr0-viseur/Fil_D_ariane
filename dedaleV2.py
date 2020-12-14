Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@Retr0-viseur 
PierreDubosq
/
cc_fil_d_ariane_python
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
cc_fil_d_ariane_python/dedale.py /

pierre@dubosq.eu Finished
Latest commit 098eb73 on 21 May
 History
 0 contributors
141 lines (122 sloc)  3.41 KB
  
from tkinter import *

incr = 2
size = incr * 5
posX = 1
posY = 1
map = [[]] * 100

for value in range(0, 100):
    map[value] = [0] * 100

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x * (incr), 0, x * (incr), canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y * (incr), canvas_width, y * (incr), fill="#476042")

def right():
    global posX
    global posY
    if (map[posY][posX + 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def left():
    global posX
    global posY
    if (map[posY][posX - 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX -= 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def up():
    global posY
    global posX
    if (map[posY - 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY -= 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def down():
    global posY
    global posX
    if (map[posY + 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)

def countPath():
    branching = 0
    if (map[posY + 1][posX] == 0 or map[posY + 1][posX] == 2):
        branching = branching + 1
    if (map[posY - 1][posX] == 0 or map[posY - 1][posX] == 2):
        branching = branching + 1
    if (map[posY][posX + 1] == 0 or map[posY][posX + 1] == 2):
        branching = branching + 1
    if (map[posY][posX - 1] == 0 or map[posY][posX - 1] == 2):
        branching = branching + 1
    return branching

def move():
    if (map[posY + 1][posX] == 0 or map[posY + 1][posX] == 2):
        down()
    elif (map[posY - 1][posX] == 0 or map[posY - 1][posX] == 2):
        up()
    elif (map[posY][posX + 1] == 0 or map[posY][posX + 1] == 2):
        right()
    elif (map[posY][posX - 1] == 0 or map[posY][posX - 1] == 2):
        left()

dir = []

def algo(value):
    global posY
    global posX
    branching = countPath()
    if branching > 1:
        dir.append([posY, posX])
        move()
    elif branching == 0:
        setACaseXY(posX, posY, 'grey')
        posY = dir[len(dir) - 1][0]
        posX = dir[len(dir) - 1][1]
        dir.pop()
    else:
        move()

def setACaseXY(X, Y, color):
    points = [X * size, Y * size, size * (X + 1), Y * size, size * (X + 1), size * (Y + 1), X * size, size * (Y + 1)]
    w.create_polygon(points, outline="#476042", fill=color, width=4)

master = Tk()
canvas_width = 1000
canvas_height = 1000
w = Canvas(master,
           width=640,
           height=310)

path = 'map.txt'
with open(path) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       x = line.find('x')
       while x != -1:
           setACaseXY(x, cnt, 'red')
           map[cnt][x] = 1
           x = line.find('x', x + 1)
       line = fp.readline()
       cnt += 1

w.pack()

setACaseXY(47, 21, 'green')
map[21][47] = 2

for value in range(0, 1000):
    master.after(value * 100, algo, value)

checkered(w,10)

mainloop()
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
