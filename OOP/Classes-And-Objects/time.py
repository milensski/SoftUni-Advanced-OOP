class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours,minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self,hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = str(self.hours)
        mm = str(self.minutes)
        ss = str(self.seconds)
        if self.hours < 10:
            hh = f'0{self.hours}'
        if self.minutes < 10:
            mm = f'0{self.minutes}'
        if self.seconds < 10:
            ss = f'0{self.seconds}'

        return f"{hh}:{mm}:{ss}"

    def next_second(self):

        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0
            if self.minutes + 1 > Time.max_minutes:
                self.minutes = 0
                if self.hours + 1 > Time.max_hours:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
