# 绘制数轴的代码如下：
from turtle import setup, reset, pu, pd, bye, left, right, fd, bk, screensize
from turtle import goto, seth, write, ht, st, home, dot, pen

#width, height = 600, 400   # 窗口的宽度和高度（单位为：像素）
#setup(width, height, 0, 0)
SCALE = 50

def draw_axis(width, height, scale, padding=20, mark_line_length=10, show_arrow=True,
              text_offset=20, arrow_length=10, arrow_degree=30,
              mark_minor_length=6,
              mark_minor_interval=5,
              draw_minor_marker=False,
              ):    
    delta_x = 5
    max_x = width/2 - padding  # x轴最大值
    min_x = -1 * max_x
    reset()
    # draw line
    pu()       # 提起画笔，暂停绘图
    home()     # Move turtle to the origin – coordinates (0,0) 移动小海龟至初始位置
               # and set its heading to its start-orientation  并设置朝向为初始朝向
    goto(min_x, 0)  # go to the left end of the line  移动海龟到坐标轴直线的最左端
    pd()       # 落下画笔，准备绘图
    goto(max_x, 0)  # go to the right end of the line 移动海龟到坐标轴直线的最右段

    # draw mark 绘制刻度线
    cur_x = min_x                                
    while cur_x <= max_x:
        if cur_x % mark_minor_interval == 0:
            pu()
            goto(cur_x, 0)
            pd()
            if cur_x % scale == 0:
                goto(cur_x, mark_line_length)         # 绘制刻度线

                pu()  
                text_pos_x = cur_x
                if cur_x == 0:
                    text_pos_x = cur_x + 10
                goto(text_pos_x, -text_offset)
                pd()
                text = str(cur_x//scale)
                write(text, align="center")      # 书写刻度值

            elif cur_x - min_x > max_x % scale and max_x - cur_x > max_x % scale:
                if draw_minor_marker:
                    goto(cur_x, mark_minor_length)


        cur_x += delta_x

    pu()
    goto(cur_x, -text_offset)
    write("x", align="center", font=("Times New Roman", 10, "italic"))
    if show_arrow:
        # draw arrow
        arrow_x, arrow_y = max_x - 10, -5
        pu()
        goto(max_x, 0)
        pd()
        goto(arrow_x, arrow_y)
        pu()
        goto(max_x, 0)
        pd()
        goto(arrow_x, -arrow_y)

    ht()
    return


def mark(x, size, color, scale=SCALE, show_num=False): # mark是方法名，
                                 # x, size, color, scale在方法内部使用的可以变化的参数
    pos = x * scale       # 计算要移动到的新位置
    pu()                  # 提起画笔
    goto(pos, 0)          # 移动到新位置
    pd()                  # 落下画笔
    dot(size, color)      # 用给定的size和color标记
    if show_num:
        pu()                  # 提起画笔
        goto(pos, 10)         # 移动到当前位置上方10个像素
        pd()                  # 再次落下画笔
        pen(pencolor=color, pensize="5")  # 设置画笔的颜色和线的粗细
        write(str(x), align="center", font=("Arial", 10, "normal")) # 当前位置书写数字   
    
    return