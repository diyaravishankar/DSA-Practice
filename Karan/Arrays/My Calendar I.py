from sortedcontainers import SortedDict
class MyCalendar:
    def __init__(self):
        self.calendar = SortedDict()
    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right(start)
        if idx > 0:
            prev_start, prev_end = self.calendar.peekitem(idx - 1)
            if prev_end > start:
                return False
        if idx < len(self.calendar):
            next_start, _ = self.calendar.peekitem(idx)
            if end > next_start:
                return False
        self.calendar[start] = end
        return True