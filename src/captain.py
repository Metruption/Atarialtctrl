'''
1;5004;0c1;5003;0cthis shit is gonnA BE LIKE MAINNN

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
    def __init__(self):
        self.ready = False
        self.map_ = {}
        #i want like a fucking fuck what do i
        #im sorry
        joys = [Joystick(31,33,35,37,40),Joystick(7,11,13,15,12)]
        self.unset = joys[0].FAL()+joys[1].FAL()

    def stupid(self, shit): #xd
        '''
    so bascically this converts button status (1 for pressed 0 for not pressed)
    into gpio signals that the atari can see
    as it turns out we want to swap them
    i could just have them be converted to booleans and then do !whatever
    hey aaron do that if the shit is laggy
    '''
        shit = int(shit)#fuck
        if shit == 0:
            return 1
        if shit == 1:
            return 0

    def handle_input(self, line):
        #handles input from main and makes the shit happen
        def split(line): #NOTE TO FUCKING SELF: TYPE 03 INPUT EVENTS ARE ANALOG AND TYPE 01 ARE DIGITAL, IGNORE ALL OTHERS AND IM STUPID FOR WRITING CODE TO DETECT ANALOG INPUTS BASED ON THEIR VALUE FUCK ME if the code is slow optimize it by changing how it filters analog input
            """
            PRECONDITIONS: @param line is an event in text form
            POSTCONDITIONS: ret

urns a dict with a few key bits
p                "button_id" is an ugly ass string
                "button_status" is the number that indicates wahts gonig on
          """
            if "code 00" in line:
                return "FUCK"
            bits = line.strip().split(',')#bits meaning parts of the line, not actual bits
            if "type 00" in bits or "type 04" in bits:
                return None
            else:#YEAH IT FUCKING LIKE doesnt needd to exist but its for code readability in this wasteland
                val =  bits[-1].split(" ")[-1]
                nomen = bits[0]+bits[2]
                type_ = int(bits[3].strip()[-2:]) #UNCOMMENT THIS LINE WHEN U DO THE ANALOG OPTIMIZATION #thank you past me (for the first and only time)
                return {"id":nomen,"status":int(val),"type":type_}

        def filter_(input_):
            """
            PRECONDITIONS: @param input) is a split line
            POSTCONDITIONS: doesnt fuck with digital inputs
            makes us ignore analog inputs below the threshold (todo add a threshhold)

            so if we are ignoring this input return None NO ACTUALLY
WHAT WE DO IS WE JUST FUCKING PRETEND THOSE ARE ALL ZERO FUCKING DUHH
if we are keeping this input and its analog we convert it to "simple analog" where it's 1, 0, or -1 where 1 is "up OR left", 0 is in dead zone, -1 is "down or right"
            some digital dpads use this already so it makes sense

#todo(aaron) unfuck this formatting
            """
            if input_ == "FUCK":
                return input_
            if input_["status"]>300:
                print(input_["status"],"FUCKING SORRY")
                return "FUCK" #uncodumented bullshit sorry
                #ok some documentation about when we fuck inputs:
                #for some reason one of my controllers gives us an input status
                #of like fifty thousand and then the program crashes
                #or worse, it keeps running nd thinks we should bind that to a button


            if input_["type"] == 3: #3 seems to mean analog
 #               print("sorry no analogs today ahahah")
#                return None
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

        line = split(line)
        line = filter_(line)
        if line == "FUCK":
            print("FUCKED AN INPUT")
            return 1 #fuck this crappy snes knockoff, returning 1 to indicate a different exit statuss
        print("parsing this line",line)
        if self.ready:
            if line["id"] in self.map_.keys():
                self.map_[line['id']](int(self.stupid(line["status"])))
        if not self.ready:
            #we want to split the line into 3 parts and also filter
            if line["id"] not in self.map_.keys():
                print("bound one",len(self.unset))
                self.map_[line["id"]] = self.unset[0]
                self.unset = self.unset[1:]
                if len(self.unset) == 0:
                    print("ITS FUCKING READY NOW!!")
                    print(self.map_)
                    self.ready = True




def main():
    f = open("evs")
    devices = ["/dev/input/"+line for line in f.read().split("\n")][:-1]
    print(devices)
    print("fucking debug my ass")
    devices = map(InputDevice, devices)
    devices = {dev.fd: dev for dev in devices}

    joy2_pins = [12,7,11,13,15]#this is the right controller, player2
    jo1_pins = [40,31,33,35,37]#this is the left conroller, player1

    '''
    so now i need to map
the shits
like fucking
    '''

    cap = JoyCaptain() #fuck i forgot about main existing, i'm sorry that i hardcoded the pins in there
    while True:
        r, w, x = select(devices, [], [])
        for fd in r:
            for event in devices[fd].read():
                cap.handle_input(str(fd)+","+str(event))

if __name__ == "__main__":
    main()
