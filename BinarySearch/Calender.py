class MyCalendar:

    def __init__(self):
        self.booking=[]

    def book(self, start: int, end: int) -> bool:
        # im guessing lowerbound
        if not self.booking:
            self.booking.append((start,end))
            return True
        else:
            index=bisect.bisect_left(self.booking,(start,end))
            if index-1>=0 and self.booking[index-1][1]>start or index<len(self.booking) and self.booking[index][0]<end:
                return False
            else:
                if index<len(self.booking):
                    self.booking.insert(index,(start,end))
                else:
                    self.booking.append((start,end))
                return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
            

# Input
# ["MyCalendar","book","book","book","book"]
# [[],[2,3],[10,20],[5,10],[20,30]]
            
# Output
# [null,true,true,true,true]
