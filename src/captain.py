'''
this shit is gonnA BE LIKE MAINNN
'''

'''
anything from `ls /dev/input | grep event` should get wachet
'''
from evdev import InputDevice
from select import select

class JoyCaptain:
    pinkey=["fire","up","left","down","right"]
    DOWN = 0
    UP = 1 #these two constants are how to handle gpio pins
    #so when we press a button we set its associated gpio pin(s) to DOWN aka 0 to make the atari think that its controller pin is grounded
    #and then we set the pin to 1 when we relese the pin so the atari thinks we released the button
    #what the fuck this is so cool
    def __init__(self, j1p, j2p):
        self.ready = False
        self.map = {}
        #begin NOT REAL CODE
        #i want like a fucking fuck what do i want
        #end NOT REAL CODE

    def handle_input(self, line)
        #handles input from main and makes the shit happen
        def split(line):
            """
            PRECONDITIONS: @param line is an event in text form
            POSTCONDITIONS: returns a dict with a few key bits
                "button_id" is an ugly ass string
                "button_status" is the number that indicates wahts gonig on
          """
            pass #todo weite this
        def filter(input_):
            """
            PRECONDITIONS: @param input) is a split line
            POSTCONDITIONS: doesnt fuck with digital inputs
            makes us ignore analog inputs below the threshold (todo add a threshhold)
            so if we are ignoring this input return None
if we are keeping this input and its analog we convert it to "simple analog" where it's 1, 0, or -1 where 1 is "up OR left", 0 is in dead zone, -1 is "down or right"
            some digital dpads use this already so it makes sense
            
#todo(aaron) unfuck this formatting
            """
            pass #todo write this

        if self.ready:
            pass #write this after you do not ready
        if not self.ready:
            #we want to split the line into 3 parts and also filter it




            
def main():
    f = open(evs)
    devices = (line for line in f)
    devices = map(InputDevice, devices)
    devices = {dev.fd: dev for dev in devices}

    joy2_pins = [12,7,11,13,15]#this is the right controller, player2
    jo1_pins = [40,31,33,35,37]#this is the left conroller, player1

    '''
    so now i need to map
the shits
like fucking
    '''

    joy
