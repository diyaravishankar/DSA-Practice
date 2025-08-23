import heapq
class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []
        counts = [0] * n
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            duration = end - start
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                earliest_end, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (earliest_end + duration, room))
            counts[room] += 1
        max_meetings = max(counts)
        for i in range(n):
            if counts[i] == max_meetings:
                return i