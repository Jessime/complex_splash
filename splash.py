# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:40:52 2016

@author: jessime
"""

import graphics
import time
import random
import pickle

def wait_on_enter():
    entered = False
    while not entered:
        key = win.getKey()
        if key == 'Return':
            entered = True

#Setup window
win = graphics.GraphWin("Complex Splash", 600, 400)
win.setBackground('white')

#Intro
t = graphics.Text(graphics.Point(300,50), "Welcome to Complex Splash!!")
t2 = graphics.Text(graphics.Point(300,200), "In this game you will  be able to learn and have fun at the same time!")
t.setFace('arial')
t.setTextColor('red')
t.setSize(32)
t2.setFace('arial')
t.draw(win)
t2.draw(win)
win.getMouse()
t.undraw()
t2.undraw()

#Main menu
#Username
menu_prompt = graphics.Text(graphics.Point(300,50), "Please Enter Your Username")
menu_prompt.draw(win)
menu_entry = graphics.Entry(graphics.Point(300, 100), 10)
menu_entry.draw(win)
wait_on_enter()
player = menu_entry.getText()
t2.setText('Greetings, young {}!'.format(player))
t2.draw(win)
menu_entry.setText('')

#Difficulty
menu_prompt.setText('Select A difficulty between 0 and 50')
difficulty = None
while not difficulty:
    wait_on_enter()
    input_difficulty = menu_entry.getText()
    try:
        input_difficulty = int(input_difficulty)
    except ValueError:
        pass
    menu_entry.setText('')
    if 0 <= input_difficulty <= 50:
        difficulty = 60 - input_difficulty
    else:
        t2.setText('{} is not a valid difficulty'.format(input_difficulty))
if difficulty > 30:
    t2.setText('This should be easy')        
else:
    t2.setText('This might be hard')
menu_entry.undraw()
time.sleep(1)
t2.undraw()
    
#Dunked head
menu_prompt.setText('Select a person to be dunked')
dj = graphics.Image(graphics.Point(130, 150), 'dj.gif')
jk = graphics.Image(graphics.Point(300, 150), 'jk.gif')
bm = graphics.Image(graphics.Point(470, 150), 'bm.gif')
dj.draw(win)
jk.draw(win)
bm.draw(win)

#Dunk Button 1
dunk1 = graphics.Text(graphics.Point(130, 300), 'Dunk!')
dunk1_box = graphics.Rectangle(graphics.Point(105, 290), graphics.Point(150, 310))
dunk1_box.setFill('light blue')
dunk1_box.draw(win)
dunk1.draw(win)

#Dunk Button 1
dunk2 = dunk1.clone()
dunk2_box = dunk1_box.clone()
dunk2.move(170, 0)
dunk2_box.move(170, 0)
dunk2_box.draw(win)
dunk2.draw(win)

#Dunk Button 3
dunk3 = dunk1.clone()
dunk3_box = dunk1_box.clone()
dunk3.move(340, 0)
dunk3_box.move(340,0)
dunk3_box.draw(win)
dunk3.draw(win)

#wait for button click
button_clicked = None
while not button_clicked:
    loc = win.getMouse()
    if 105 <= loc.x <= 150 and 290 <= loc.y <= 310:
        button_clicked = 1
    elif 105+170 <= loc.x <= 150+170 and 290 <= loc.y <= 310:
        button_clicked = 2
    elif 105+340 <= loc.x <= 150+340 and 290 <= loc.y <= 310:
        button_clicked = 3

#Undraw everything but the dunk image
dunk1.undraw()
dunk2.undraw()
dunk3.undraw()
dunk1_box.undraw()
dunk2_box.undraw()
dunk3_box.undraw()
if button_clicked == 1:
    jk.undraw()
    bm.undraw()
elif button_clicked == 2:
    dj.undraw()
    bm.undraw()
elif button_clicked == 3:
    dj.undraw()
    jk.undraw()

#Wait for click before starting the game
menu_prompt.undraw()
t.setText('Click to Start!')
t.draw(win)
win.getMouse()

#setup text for questions
t.undraw()
menu_prompt.setText('')
menu_prompt.draw(win)
menu_entry.draw(win)
t2.setText('')
t2.draw(win)
if button_clicked == 1:
    dj.undraw()
elif button_clicked == 2:
    jk.undraw()
elif button_clicked == 3:
    bm.undraw()

#load questions
qa = pickle.load(open('questions.txt'))

#set time and score for questions
current_time = time.time()
end_time = current_time + difficulty
num_correct = 0

#Start asking question
while current_time < end_time and num_correct != 3:
    #Generate question and answer
    question = random.sample(qa,1)[0]
    answer = qa[question].lower()
    menu_prompt.setText(question)
    
    #Check if answer is correct    
    wait_on_enter()
    guess = menu_entry.getText().lower()
    if guess == answer and time.time() < end_time:
        num_correct += 1
        t2.setText('Correct! +1 for {}.'.format(player))
    else:
        t2.setText('Sorry. The answer isn\'t {}, it is {}'.format(guess, answer))
    menu_entry.setText('')
    current_time = time.time()
print num_correct
win.getMouse()
win.close()