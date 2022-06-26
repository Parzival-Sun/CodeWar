def divide_seconds(divided, divider):
    return divided // divider, divided % divider


def add_into_time_result(res, unit, q):
    if q > 1:
        add_s = 's'
    else:
        add_s = ''

    if unit == 0:  # Year
        res['year' + add_s] = q
    elif unit == 1:  # Day
        res['day' + add_s] = q
    elif unit == 2:  # Hour
        res['hour' + add_s] = q
    elif unit == 3:  # Minute
        res['minute' + add_s] = q
    elif unit == 4:  # Second
        res['second' + add_s] = q


def format_duration(seconds):
    time_units = [365 * 24 * 60 * 60, 24 * 60 * 60, 60 * 60, 60, 1]
    time_result = {}
    if seconds is 0:
        return "now"
    for rounds in range(5):
        quo, rem = divide_seconds(seconds, time_units[rounds])
        seconds -= (quo * time_units[rounds])
        if quo > 0:
            add_into_time_result(time_result, rounds, quo)
    countdown = len(time_result)
    output_str = ''
    for key in time_result:
        if countdown > 2:
            output_str += str(time_result[key]) + ' ' + key + ', '
        elif countdown == 2:
            output_str += str(time_result[key]) + ' ' + key + ' and '
        else:
            output_str += str(time_result[key]) + ' ' + key
        countdown -= 1

    return output_str


print(format_duration(1), "1 second")
print(format_duration(62), "1 minute and 2 seconds")
print(format_duration(120), "2 minutes")
print(format_duration(3600), "1 hour")
print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
print(format_duration(0), "now")

test = ['first, third']
test 1 test 2 find some thing tty
to practicefind


1. 匿名暫存器 (The unnamed register) ""
Gsmall匿名暫存器smallsmallsmallGuu3. (The  delete regster) "-
匿名暫存器

abcdefg00 [something test bc]
test "test this is a word" abc
() test