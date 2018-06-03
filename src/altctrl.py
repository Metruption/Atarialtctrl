"""
Atarialttrl: python code to control an atari2600 car using an rpi
    Copyright (C) 2018 Aaron Thomas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Joystick:
    """
    Each varaiable passed to Joystick's init represents the pin number on the
    rpi that is connected to an assosicated pin on the atari2600. For more info
    on which pins on the atari2600 do what look at the atari2600 pin image in
    this repo.
    This class emulates a standard atari joystick controller with a fire button
    If you try to hold up+down or left+right weird things may happen
    """
    def __init__(self, fire, up, down, left, right):
        self.fire = fire
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        GPIO.setup(fire, GPIO.OUT)
        GPIO.setup(up, GPIO.OUT)
        GPIO.setup(down, GPIO.OUT)
        GPIO.setup(left, GPIO.OUT)
        GPIO.setup(right, GPIO.OUT)

        GPIO.output(fire, GPIO.HIGH)
        GPIO.output([up,down,left,right], GPIO.HIGH) #these are all high when the joystick is in neutral position


        '''
        if you send a state that isn't 1,0,True,False,GPIO.LOW, or GPIO.HIGH
        and then something bad happens then it's your fault
        not because I say so, but because of the GPL license that provides no warranty
        '''
    def set_up(self, state):
        GPIO.output(self.up,state)

    def set_down(self, state):
        GPIO.output(self.down,state)

    def set_left(self, state):
        GPIO.output(self.left,state)

    def set_right(self, state):
        GPIO.output(self.right,state)

    def set_fire(self, state):
        GPIO.output(self.fire,state)


    def FAL(self): #im so sorry but this is the laziest way forme to code this and i just want it to work
        return [self.set_up,self.set_down,self.set_left,self.set_right,self.set_fire]
