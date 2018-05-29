import altctrl
import time


"some fuckin test scripts to let me easily tap a button and such"


'''
the pins im using
the grounds are all connected so thats nice
UP DOWN LEFT RIGHT FIRE
joy1 is 7,11,13,15,12
joy2 is 31,33,35,37,40
'''

fire = 40
up = 31
down = 33
left = 35
right = 37
#fuck the lack of semicolons bothers me
#i should just do everything in rust
#but first i need to learn rust (shrugging emoticon)
#eah its an emoticon, fight me
#emoji is a specific subset of unicode
#now i havent even written any code, just shitposted in the commends
#this is what coding is all about!
#btw emacs rules and i'm using emacs right fuckin now

joy = altctrl.Joystick(fire,up,down,left,right)

#ok so t"shit" just means i'm tapping it real quickly
#tbh its gonna be easy





                   
def tfire():       
    joy.set_fire(0)
    time.sleep(1)
    joy.set_fire(1)

def tup():       
    joy.set_up(0)
    time.sleep(1)
    joy.set_up(1)
                                  
def tdown():       
    joy.set_down(0)
    time.sleep(1)
    joy.set_down(1)

def tleft():   
    joy.set_left(0)
    time.sleep(1)
    joy.set_left(1)

def tright():   
    joy.set_right(0)
    time.sleep(1)
    joy.set_right(1)
    

def exit():
    GPIO.cleanup()
    quit()
