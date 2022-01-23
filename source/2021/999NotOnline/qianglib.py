from turtle import setup, reset, pu, pd, bye, left, right, fd, bk, screensize
from turtle import goto, seth, write, ht, st, home, dot, pen, speed

from turtle import setworldcoordinates, begin_fill, end_fill


def text(pos, info, align="center", font=("Arial", 8, "normal"), move=False, color="black"):
    pu()
    goto(pos)
    pd()
    pen(pencolor=color)
    write(info, move=move, align=align, font=font)


def mark(pos, info=None,
         size=5, color="red", offset=(0.5, 0.5), align="left", 
         font=("Arial", 10, "normal"), move=False, ):
    pu()
    goto(pos)
    pd()
    dot(size, color)
    if info is not None:
        if offset is not None:
            pu()
            goto(add_v(pos, offset))
            pd()
        pen(pencolor=color)
        info = str(pos) if info is None else info
        write(info, move=move, align=align, font=font)
    return
    
    
def line(start, end, line_width=1, color="black"):
    pu()
    old_speed = speed()
    goto(start)
    pen(pencolor=color, pensize=line_width)
    pd()
    goto(end)
    speed(old_speed)
    
    
def lines(points, line_width=1, color="black", fillcolor=None, closed=False):
    if len(points) < 2:
        return
    pu()
    goto(points[0])
    pen(fillcolor=fillcolor, pensize=line_width, pencolor=color)
    pd()
    extra = 1 if closed else 0
    for i in range(1, len(points)+extra):
        goto(points[i%len(points)])
        
    
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
        line((min_x, i), (max_x, i), line_width=pensize, color=line_color)
        
    # draw vertical grid
    for i in range(min_x + 1, max_x):
        pensize = minor_grid_pen_size
        line_color = minor_grid_color
        if i % 5 == 0:
            pensize = major_grid_pen_size
            line_color = major_grid_color
            text((i, min_y-1), str(i), align="center", color=outline_color)
            text((i, max_y), str(i), align="center", color=outline_color)
        line((i, min_y), (i, max_y), line_width=pensize, color=line_color)

    # draw outline
    points = [(min_x, min_y),(max_x, min_y),(max_x, max_y),(min_x, max_y)]
    polygon(points, line_width=outline_pen_size, color=outline_color, fillcolor=None)
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
    
def get_center(points):
    x, y = 0, 0
    for point in points:
        x += point[0]
        y += point[1]
    return x/len(points), y/len(points)

def add_v(point1, point2):
    return point1[0]+point2[0], point1[1]+point2[1]

def polygon(points, line_width = 3, color="black", fillcolor=None, 
              side_texts=None, 
              side_text_font = ("Arial", 12, "italic"),
              side_text_offsets=[(0, -1), (0.5, -0.5), (0, 0), (-0.5, -0.5)],
              side_text_color="black",
              center_text="", 
              center_text_font=("Arial", 16, "italic"),
              center_text_offset=(0, -0.5),
              center_text_color="black",
              marker_texts=None,
              marker_offsets=None,
              marker_text_font = ("Arial", 16, "italic"),
              marker_text_color = "red",
              marker_dot_size = 5):
    
    if len(points) < 3:
        return
    begin_fill()
    lines(points, line_width=line_width, color=color, fillcolor=fillcolor, closed=True)
    end_fill()
    
    for i in range(len(points)):
        if marker_texts is not None and i<len(marker_texts) and \
        marker_texts[i] is not None:
            marker_offset = (0, 0)
            if marker_offsets is not None and i < len(marker_offsets) and \
            marker_offsets[i] is not None:
                marker_offset = marker_offsets[i]
            
            mark(points[i], marker_texts[i], 
                 size=marker_dot_size, color=marker_text_color,
                 offset=marker_offset)
            
        if side_texts is not None and i<len(side_texts) and \
        side_texts[i] is not None:
            side_text_offset = (0, 0)
            if side_text_offsets is not None and i < len(side_text_offsets) and \
            side_text_offsets[i] is not None:
                side_text_offset = side_text_offsets[i]
                
            point1 = points[i]
            point2 = points[(i+1)%len(points)]
            center = get_center([point1, point2])
            mark_pos = add_v(center, side_text_offset)
            text(mark_pos, side_texts[i], align="center", 
                 font=side_text_font, color=side_text_color)
    
    if center_text is not None and center_text != "":  
        if center_text_offset is None:
            center_text_offset = (0, 0)
        center_pos = add_v(get_center(points), center_text_offset)
        text(center_pos, center_text, align="center",
             font=center_text_font, color=center_text_color)
    return

def rectangle(points, line_width = 1, color="black", fillcolor=None, 
              side_texts=["a", "b"], 
              side_text_font = ("Arial", 12, "italic"),
              side_text_offsets=[(0, -1), (0.5, -0.5), (0, 0), (-0.5, -0.5)],
              side_text_color="black",
              center_text="center", 
              center_text_font=("Arial", 16, "italic"),
              center_text_offset=(0, -0.5),
              center_text_color="black",
              marker_texts=list("ABCD"),
              marker_text_font = ("Arial", 16, "italic"),
              marker_text_color = "red",
              marker_dot_size = 5,
              marker_offsets=[1, 1, 0, 0],
              marker_offset_directions=[-90, -90, 45, 45]):
    polygon(points, line_width = line_width, color=color, fillcolor=fillcolor,
            side_texts=side_texts,
            side_text_font = side_text_font,
            side_text_offsets=side_text_offsets,
            side_text_color=side_text_color,
            center_text=center_text, 
            center_text_font=center_text_font,
            center_text_offset=center_text_offset,
            center_text_color=center_text_color,
            marker_texts=marker_texts,
            marker_text_font = marker_text_font,
            marker_text_color = marker_text_color,
            marker_dot_size = marker_dot_size,
            marker_offsets=marker_offsets,
            marker_offset_directions=marker_offset_directions
           )
    return
    
        

def generate_parallelogram(p_left_bottom, base, height, hor_offset):
    p_right_bottom = (p_left_bottom[0]+base, p_left_bottom[1])
    p_right_top = (p_right_bottom[0]+hor_offset, p_right_bottom[1]+height)
    p_left_top = (p_right_top[0]-base, p_right_top[1])
    parallelogram = [p_left_bottom, p_right_bottom, p_right_top, p_left_top]
    return parallelogram  

def generate_rectangle(p_left_bottom, base, height):
    return generate_parallelogram(p_left_bottom, base, height, 0)


def translate(shape, offset):
    '''move a shape certain distance defined by offset
    params:
        shape: a point, line, or a polygon;
               data type: tuple or list of tuple
               example: (2, 4), [(1, 2), (3, 5)], [(1, 2), (3, 5), (5, 6)]
        offset: distance
               data type: tuple (dx, dy)
               example: (9, 9)
    return a tuple or list of tuple representing a point, or a line, polygon.
    '''
    new_shape = None
    if type(shape) == tuple:  # a point
        new_shape = shape[0]+offset[0], shape[1]+offset[1]
    elif type(shape) == list: # a line or a polygon
        new_shape = []
        for point in shape:
            new_point = point[0] + offset[0], point[1]+offset[1]
            new_shape.append(new_point)
    else:
        pass
    return new_shape  


def mirror(shape, symmetry_axis):
    '''mirror a shape based on a horizontal or vertical symmetry_axis 
       represented by two points
    params:
        symmetry_axis: list of point, lenth = 2, either horizontal or vertical
               data type: [(int, int), (int, int)]
               example: [(0, 13), (38, 13)] a horizontal line
        offset: shape, a point, line, or a polygon
               data type: tuple or list of tuple
               example: (2, 4), [(1, 2), (3, 5)], [(1, 2), (3, 5), (5, 6)]
               
    return a tuple or list of tuple representing a point, or a line, polygon.
    '''
    new_shape = None
    is_axis_horizontal = False
    is_axis_vertical = False
    if len(symmetry_axis) != 2:
        return None
    if symmetry_axis[0][0] == symmetry_axis[1][0]:
        is_axis_vertical = True # vertical
    if symmetry_axis[0][1] == symmetry_axis[1][1]:
        is_axis_horizontal = True
    if not is_axis_horizontal and not is_axis_vertical:
        return None  # don't know how to mirror so far
    
    the_value, the_index = None, None
    if is_axis_horizontal:
        the_value = symmetry_axis[0][1] # a y value
        the_index = 1 # will update y value
    else:
        the_value = symmetry_axis[0][0]
        the_index = 0 # will update x value
        
    if type(shape) == tuple:  # a point
        new_value = 2*the_value - shape[the_index]
        new_shape = list(shape)
        new_shape[the_inex] = new_value
        new_shape = tuple(new_shape)
    elif type(shape) == list: # a line or a polygon
        new_shape = []
        for point in shape:
            new_value = 2*the_value - point[the_index]
            new_point = list(point)
            new_point[the_index] = new_value
            new_point = tuple(new_point)
            new_shape.append(new_point)
    else:
        pass
    return new_shape  