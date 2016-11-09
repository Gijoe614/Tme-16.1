class Time:
    """Represents the time of day
    attributes: hour, minute, second
    """

    def __init__(self):
        pass


def print_time(t):
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print ('The hour field is 11, the minute field is 59, and the second field is 30. \n')
print ('This input will be reformatted to a conventional format: \n')

print_time(time)
