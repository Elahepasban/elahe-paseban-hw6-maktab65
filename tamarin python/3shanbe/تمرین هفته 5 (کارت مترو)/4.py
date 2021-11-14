class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def int_to_time(self):
        time = (self.hour * 3600) + (self.minute * 60) + self.second
        return time

    @classmethod
    def time_to_int(cls, seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = (seconds % 3600) % 60
        return cls(h, m, s)

    def add_time(self, other):
        times_1 = self.int_to_time() + other.int_to_time()
        times_2 = Time.time_to_int(times_1)
        return f" times: {times_2.hour}:{times_2.minute}:{times_2.second}"

    def __str__(self):
        return f"{self.hour}, {self.minute}, {self.second}"


t1 = Time(21, 15, 20)
print(t1.int_to_time())
print(Time.time_to_int(3600))
t2 = Time(20, 30, 14)
print(t1.add_time(t2))
