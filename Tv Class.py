class Tv :
    def __init__(self) :
        self.channel = 1   # Default channel is 1
        self.volumelevel = 1 # Default volume is 1
        self.on = False    # Initially, TV is off

    def turnOn(self) :
        self.on = True

    def turnOff(self) :
        self.on = False

    def getChannel(self) :
        return self.channel
    
    def setChannel(self, channel) :
        if self.on and 1 <= self.channel <= 120 :
            self.channel = channel

    def getVolumeLevel(self) :
        return self.volumelevel
    
    def setVolume(self, volumeLevel) :
        if self.on and 1 <= self.volumelevel <= 7 :
            self.volumelevel = volumeLevel

    def channelUp(self) :
        if self.on and self.channel < 120 :
            self.channel += 1

    def channelDown(self) :
        if self.on and self.channel > 1 :
            self.channel -= 1

    def volumeUp(self) :
        if self.on and self.volumelevel < 7 :
            self.volumelevel += 1

    def volumeDown(self) :
        if self.on and self.volumelevel > 1 :
            self.volumelevel -= 1


tv1 = Tv()   # Invokes the methods on the objects 
tv1.turnOn()
tv1.setChannel(30)
tv1.setVolume(3)

tv2 = Tv()
tv2.turnOn()
tv2.channelUp()
tv2.channelUp()
tv2.volumeUp ()
tv2.volumeUp ()
tv2.volumeUp ()

print("TV 1's channel is", tv1.getChannel(), 
        "and volume level is", tv1.getVolumeLevel())

print("TV 2's channel is", tv2.getChannel(), 
        "and volume level is", tv2.getVolumeLevel())
        
# main() # Call the main function