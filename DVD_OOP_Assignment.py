class DVD:
    def __init__ (self,power,start_stop,tray_state,max_chapter):
        self.power = power
        self.tray_state = tray_state
        self.start_stop = start_stop
        self.chapter = 1
        self.last_chapter = max_chapter

    def power_button (self):
        if self.power == "off":
            self.power = "on"
        else:
            self.power = "off"

    def pause (self):
        self.start_stop = "stop"

    def resume (self):
        self.start_stop = "start"

    def tray (self):
        if self.tray_state == "closed":
            self.tray_state = "open"
        else:
            self.tray_state = "closed"

    def skip (self):
        if self.chapter < self.max_chapter:
            self.chapter += 1
        else:
            self.chapter = 1

DVD_player = DVD ("off","start","closed",10)