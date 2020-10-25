#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

Revised by S. Urista
Oct 2020
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

Revised by S. Urista
Oct 2020
"""


class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        # revised to non-military time, adds AM/PM- S. Urista

        if self.hour >= 24:
            self.hour %= 24

        if self.hour >= 12:
            period = "PM"
        else:
            period = "AM"

        if self.hour > 12:
            self.hour -= 12

        return '%.1d:%.2d %s' % (self.hour, self.minute, period)  # revised by su

    def print_time(self):
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True

    def __eq__(self, other):
        return (self.hour, self.minute, self.second) == (other.hour, other.minute, other.second)


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time

# Test some of the features of Class Time - jdp
def main():    # jdp
    start = Time(0, 1, 1)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?', end=" ")
    print(end.is_after(start))

    # Testing __str__
    print(f'Using __str__: {start} {end}')

    # Testing addition
    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)

    # A time that is invalid
    t1 = Time(50)
    print(t1)

main()