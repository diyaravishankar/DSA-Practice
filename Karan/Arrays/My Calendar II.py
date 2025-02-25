class MyCalendarTwo:
    def __init__(self):
        self.doubled = []
        self.bookings = []
    def book(self, start: int, end: int) -> bool:
        for s, e in self.doubled:
            if start < e and end > s:
                return False
        for s, e in self.bookings:
            if start < e and end > s:
                self.doubled.append([max(s, start), min(e, end)])  
        self.bookings.append([start, end])
        return True