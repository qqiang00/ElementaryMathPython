from turtle import setup, reset, pu, pd, bye, left, right, fd, bk, screensize
from turtle import goto, seth, write, ht, st, home, dot, pen, speed

from turtle import setworldcoordinates, begin_fill, end_fill


def text(pos, info, align="left", font=("Arial", 8, "normal"), move=False, color="black"):
    pu()
    goto(pos)
    pd()
    pen(pencolor=color)
    write(info, move=move, align=align, font=font)


def mark(pos, info=None, 
         size=5, color="red", offset=0.5, offset_direction=45, align="left", 
         font=("Arial", 10, "normal"), move=False):
    pu()
    goto(pos)
    pd()
    dot(size, color)
    pu()
    seth(offset_direction)
    fd(offset)
    pd()
    pen(pencolor=color)
    info = str(pos) if info is None else info
    write(info, move=move, align=align, font=font)
    
    
def line(start, end, linewidth=1, color="black"):
    pu()
    old_speed = speed()
    goto(start)
    pen(pencolor=color, pensize=linewidth)
    pd()
    goto(end)
    speed(old_speed)
    
    
def lines(points, linewidth=1, color="black", fillcolor=None, closed=False):
    if len(points) < 2:
        return
    pu()
    goto(points[0])
    pen(fillcolor=fillcolor, pensize=linewidth, pencolor=color)
    pd()
    extra = 1 if closed else 0
    for i in range(1, len(points)+extra):
        goto(points[i%len(points)])
        
    
def polygon(points, linewidth = 1, color="black", fillcolor=None):
    if len(points) < 3:
        return
    begin_fill()
    lines(points, linewidth=linewidth, color=color, fillcolor=fillcolor, closed=True)
    end_fill()
    
    
def draw_grid(min_x = 0,
              min_y = 0,
              max_x = 20, 
              max_y = 15, 
              outline_color="grey",
              major_grid_color="snow3",
              minor_grid_color="snow2",
              outline_pen_size=2, 
              major_grid_pen_size=1, 
              minor_grid_pen_size=1
             ):
    old_speed = speed()
    speed(0)   
    if min_x == 0 and min_y == 0:
        text((min_x-0.2, min_y-1), "0", align="center", color=outline_color)
    
    # draw horizontal grid
    for i in range(min_y + 1, max_y):
        pensize = minor_grid_pen_size
        line_color = minor_grid_color
        if i % 5 == 0:
            pensize = major_grid_pen_size
            line_color = major_grid_color
            text((min_x-0.3, i-0.3), str(i), align="right", color=outline_color)
            text((max_x+0.3, i-0.3), str(i), align="left", color=outline_color)
        line((min_x, i), (max_x, i), linewidth=pensize, color=line_color)
        
    # draw vertical grid
    for i in range(min_x + 1, max_x):
        pensize = minor_grid_pen_size
        line_color = minor_grid_color
        if i % 5 == 0:
            pensize = major_grid_pen_size
            line_color = major_grid_color
            text((i, min_y-1), str(i), align="center", color=outline_color)
            text((i, max_y), str(i), align="center", color=outline_color)
        line((i, min_y), (i, max_y), linewidth=pensize, color=line_color)

    # draw outline
    points = [(min_x, min_y),(max_x, min_y),(max_x, max_y),(min_x, max_y)]
    polygon(points, linewidth=outline_pen_size, color=outline_color, fillcolor=None)
    ht()
    speed(old_speed)
    
    
def prepare_paper(width, height, scale=20, min_x = 0, min_y = 0, max_x=None, max_y=None):
    reset()
    max_length, max_height = int(width/scale), int(height/scale)
    setworldcoordinates(min_x-1, min_y-1, max_length-abs(min_x-1), max_height-abs(min_y-1))
    if max_x is None or max_x > max_length-abs(min_x-1)-1:
        max_x = max_length-abs(min_x-1)-1
    if max_y is None or max_y > max_height-abs(min_y-1)-1:
        max_y = max_height-abs(min_y-1)-1
    draw_grid(min_x, min_y, max_x, max_y)