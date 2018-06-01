'''
this shit is gonnA BE LIKE MAINNN
'''

'''
anything from `ls /dev/input | grep event` should get wachet
'''
from evdev import InputDevice
from select import select

from altctrl import Joystick

class JoyCaptain:
    DOWN = 0
    UP = 1 #these two constants are how to handle gpio pins
    #so when we press a button we set its associated gpio pin(s) to DOWN aka 0 to make the atari think that its controller pin is grounded
    #and then weset the pin to 1 when we relese the pin so the atari thinks we released the button
    #fucking jokes im not gonna use them
    #what the fuck this is so cool
    def __init__(self, j1p, j2p):
        self.ready = False
        self.map_ = {}
        self.analogs = [] #a list of all buttons that ahve been identified as analog


        #begin NOT REAL CODE
        #i want like a fucking fuck what do i
        #im sorry 
        joys = [Joystick(31,33,35,37,40),Joystick(7,11,13,15,12)]
        self.unset = joys[0].FAL()+joys[1].FAL
        
    def stupid(self, shit): #xd
        if shit == 0:
            return 1
        if shit == 1 or shit == -1:
            return 0

    def handle_input(self, line)
        #handles input from main and makes the shit happen
        def split(line):
            """
            PRECONDITIONS: @param line is an event in text form
            POSTCONDITIONS: ret

urns a dict with a few key bits
p                "button_id" is an ugly ass string
                "button_status" is the number that indicates wahts gonig on
          """
            pass #todo weite this
        def filter_(input_):
            """
            PRECONDITIONS: @param input) is a split line
            POSTCONDITIONS: doesnt fuck with digital inputs
            makes us ignore analog inputs below the threshold (todo add a threshhold)













            so if we are ignoring this input return None
if we are keeping this input and its analog we convert it to "simple analog" where it's 1, 0, or -1 where 1 is "up OR left", 0 is in dead zone, -1 is "down or right"
            some digital dpads use this already so it makes sense
            
#todo(aaron) unfuck this formatting
            """
            if input_["id"] not in analogs and input_["status"]>1:
                self.analogs.append(input_["id"])
            if input in analogs:
                dist = abs(input_["status"]-127) #MAGIC NUMBER i assume 127 is the neutral position for every analog input ever xd
                if dist < 20: #MAGIC NUMBER this is the dead zone where we ignore analoog inputs
                    input_["status"] = 0
                elif input_["status"] > 127:
                    input_["status"] = 1
                elif input_["status"] < 127:
                    input_["status"] = -1

            if input_["status"] == -1:
                input_["id"] = input_["id"]+"opposite"
                input_["status"] = 1
            return input_
                

        if self.ready:
            if line["id"] in self.map_.keys():
                self.map_['id'](self.stupid[line["status"])
        if not self.ready:
            #we want to split the line into 3 parts and also filter it
            line = split(line)
            line = filter_(line)
            if line["id"] not in self.map_.keys():
                self.map_[line["id"]] = self.unset[0]
                self.unset = self.unset[1:]
                if len(self.unset) == 0:
                    self.ready = True



            
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
