#Task 3 TV controller
channels = ["BBC", "Discovery", "TV1000"]
class TVController:

    def __init__(self, channels: list):
        self.channels_list = channels
        self._start_channel = channels[0]
        self._last_channel = channels[-1]
        self.actual_channel = self._start_channel


    def first1_channel(self):
        first_channel = self._start_channel
        return first_channel


    def last_channel(self):
        last_channel = self._last_channel
        return last_channel


    def turn_channel(self, number: int):
        x = number - 1
        self.actual_channel = self.channels_list[x]


    def next_channel(self):
        indx = self.channels_list.index(self.actual_channel)
        if indx == len(self.channels_list) - 1:
            self.actual_channel = self.first1_channel()
        else:
            self.actual_channel = self.channels_list[indx+1]



    def previous_channel(self):
        indx = self.channels_list.index(self.actual_channel)
        self.actual_channel = self.channels_list[indx - 1]
        if self.actual_channel == self.first1_channel:
            self.actual_channel = self._last_channel()


    def current_channel(self):
        return self.actual_channel


    def is_exist(self, num = None, name = None):
        for n in channels:
            if name in channels:
                return True
            else:
                print("No channels found")

        if num > len(self.channels_list):
            return "No"
        else:
            return "Yes"
