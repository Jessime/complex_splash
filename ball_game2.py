# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:37:21 2016

@author: jessime
"""
import graphics
import time
import random

def random_move(block, direction):
    if random.randint(0,50) == 1:
        if block.anchor.y <= 25:
            direction = 10
        if block.anchor.y >= 375:
            direction = -10
        block.move(0,direction)

def get_corners(pic):
    left = pic.anchor.x - (pic.getWidth()/2)
    top = pic.anchor.y - (pic.getWidth()/2)
    right = pic.anchor.x + (pic.getWidth()/2)
    bottom = pic.anchor.y + (pic.getWidth()/2)
    return left, top, right, bottom
    
def point_in_rect(x, y, pic):
    inside = False
    left, top, right, bottom = get_corners(pic)
    if left <= x <= right and top <= y <= bottom:
        inside = True
    return inside
    
def collision_detection(pic1, pic2):
    collision = False
    for a, b in [(pic1, pic2), (pic2, pic1)]:
        left, top, right, bottom = get_corners(a)
        if ((point_in_rect(left, top, b)) or
            (point_in_rect(left, bottom, b)) or
            (point_in_rect(right, top, b)) or
            (point_in_rect(right, bottom, b))):
            collision = True
    return collision
 
#Setup window
win = graphics.GraphWin("Complex Splash", 600, 400)
win.setBackground('white')


#Manage time    
current_time = time.time()
difficulty = 30
end_time = current_time + difficulty
display_time = graphics.Text(graphics.Point(15,10), difficulty)
display_time.setSize(24)

#Make and draw pieces
shield_x = [100, 250, 450]
ball = graphics.Image(graphics.Point(25, 150), 'water_balloon.gif')
head = graphics.Image(graphics.Point(575, 200), 'jk_small.gif')
shields = [graphics.Image(graphics.Point(x, 150), 'shield.gif') for x in shield_x]
results = graphics.Text(graphics.Point(300,50), '')
results.setSize(32)
for x in shields + [ball, head, results, display_time]:
    x.draw(win)

#Event flags
ball_num = 3
shot = False
score = False
while current_time < end_time and not score and ball_num != 0:
    
    #Check for balloon/mouse movement
    loc = win.checkMouse()
    if loc and not shot:
        ball.anchor = graphics.Point(25, loc.y)
        ball.undraw()
        ball.draw(win)
        
    #Move blocks and head
    direction = random.sample([-5, 5]*3, 4)
    random_move(head, direction[0])
    for d, s in zip(direction[1:], shields):
        random_move(s, d)
    
    
    #check for shot or movement
    last_key = win.checkKey()
    if last_key == 'space':
        shot = True

    #shoot or move balloon    
    if last_key == 'Up':
        ball.move(0, -1)
    if last_key == 'Down':
        ball.move(0, 1)
    if shot and random.randint(0, 20) == 1:
        ball.move(1, 0)
        
    #check for balloon hitting a shield or the edge
    for s in shields:
        collision = collision_detection(ball, s)
        if collision:
            break
    if (ball.anchor.x + (ball.getWidth()/2)) >= win.getWidth():
        collision = True

    #Reset or end game on miss
    if collision:
        ball_num -= 1
        win.getMouse()
        ball.undraw()
        last_key = ''
        if ball_num != 0:
            ball.anchor = graphics.Point(25,150)
            ball.draw(win)
            shot = False
            
    #check for balloon hitting head
    score = collision_detection(ball, head)
    if score:
        splash = graphics.Image(head.getAnchor(), 'splash.gif')
        splash.draw(win)
    
    #update time
    current_time = time.time()
    display_time.setText(int(end_time-current_time))

win.getMouse()
for x in shields + [ball, head, display_time]:
    x.undraw()

try:
    splash.undraw()
except AttributeError, NameError:
    pass

if score:
    results.setFill('green')
    results.setText('You Win!!!')
else:
    results.setFill('red')
    results.setText('You Lose!')
win.getMouse()
win.close()
