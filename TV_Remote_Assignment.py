class TV():
    def __init__ (self):
        self.TVpower = "Off"
        self.muted = False
        self.channels = ["02","04","05","07","09","11","20","36","44","54","65"]
        self.channelIndex = 0
        self.max_volume = 10
        self.min_volume = 0
        self.volume = 5
        self.channel = "02"
    
    def power (self):
        if self.TVpower == "On":
            self.TVpower = "Off"
        else:
            self.TVpower = "On"

    def volumeUp (self):
        if self.volume < self.max_volume:
            self.volume += 1

    def volumeDown (self):
        if self.volume > self.min_volume:
            self.volume -= 1

    def channelUp (self):
        if self.channelIndex < 10:
            self.channelIndex += 1
            self.channel = self.channels[self.channelIndex]

    def channelDown (self):
        if self.channelIndex > 0:
            self.channelIndex -= 1
            self.channel = self.channels[self.channelIndex]

    def mute (self):
        if self.muted == False:
            self.muted = True
        else:
            self.muted = False

    def showInfo (self):
        if self.TVpower == "On":
            if self.muted == False:
                print ("TV Status:\n    TV is: ",self.TVpower,"\n    Channel is: ",self.channel,"\n    Volume is: ",self.volume,"\n")
            else:
                print ("TV Status:\n    TV is: ",self.TVpower,"\n    Channel is: ",self.channel,"\n    Volume is: ",self.volume," (sound is muted)\n")
        else:
            print ("TV Status:\n    TV: is: Off\n")
    def setchannel (self,selected_channel):
        index = -1
        for i in self.channels:
            index += 1
            if selected_channel == i:
                self.channelIndex = index
                self.channel = selected_channel

oTV = TV()

oTV.power()
oTV.showInfo()

oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

oTV.volumeDown()
oTV.mute()
oTV.showInfo()

oTV.setchannel("11")
oTV.mute()
oTV.showInfo()