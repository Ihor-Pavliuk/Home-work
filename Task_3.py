#TV controller

#Create a simple prototype of a TV controller in Python. It’ll use the following commands:

#first_channel() - turns on the first channel from the list.
#last_channel() - turns on the last channel from the list.
#turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
#next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
#previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
#current_channel() - returns the name of the current channel.
#exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 

#The default channel turned on before all commands is №1.

#Your task is to create the TVController class and methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController():
    def __init__(self, channel):
        self.channel = channel
        self.channel_now = list()
         
    def first_channel(self):
        self.channel_now.append(self.channel[0])
        return self.channel[0]

    def last_channel(self):
        self.channel_now = self.channel[-1]
        return self.channel[-1]

    def turn_channel(self,n):
        if n == 1:
            self.channel_now = self.channel[0]
            return self.channel[0]
        if n == 2:
            self.channel_now = self.channel[1]
            return self.channel[1]
        if n == 3:
            self.channel_now = self.channel[2]
            return self.channel[2]
        else:
               print("Channels not exist")

    def next_channel(self):
        if self.channel_now == self.channel[0]:
            self.channel_now = self.channel[1]
            return self.channel_now
        if self.channel_now == self.channel[1]:
            self.channel_now = self.channel[2]
            return self.channel_now
        if self.channel_now == self.channel[2]:
            self.channel_now = self.channel[0]
            return self.channel_now


    def previous_channel(self):
        if self.channel_now == self.channel[2]:
            self.channel_now = self.channel[1]
            return self.channel_now
        if self.channel_now == self.channel[1]:
            self.channel_now = self.channel[0]
            return self.channel_now
        if self.channel_now == self.channel[0]:
            self.channel_now = self.channel[2]
            return self.channel_now
        
    def current_channel(self):
          return self.channel_now
    
    def exists(self,arg):
        if isinstance(arg, str):
            if arg in CHANNELS:
                return "Yes"
            else:
                return "No"
        if isinstance(arg, int):
            if arg <= 3 and arg >= 1:
                return "Yes"
            else:
                return "No"
        else: print("Not found")

controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.exists(4) == "No"
controller.exists("BBC") == "Yes"