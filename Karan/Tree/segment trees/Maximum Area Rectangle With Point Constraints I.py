from itertools import combinations
class Solution:
    def maxRectangleArea(self, points: list[list[int]]) -> int:
        pts = set((x, y) for x, y in points)
        max_area = -1
        for p1, p2, p3, p4 in combinations(points, 4):
            xs = {p1[0], p2[0], p3[0], p4[0]}
            ys = {p1[1], p2[1], p3[1], p4[1]}
            if len(xs) != 2 or len(ys) != 2: continue
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            area = (max_x - min_x) * (max_y - min_y)
            if area == 0: continue
            valid = True
            for x, y in pts:
                if min_x <= x <= max_x and min_y <= y <= max_y and (x, y) not in [(min_x,min_y),(min_x,max_y),(max_x,min_y),(max_x,max_y)]:
                    valid = False
                    break
            if valid: max_area = max(max_area, area)
        return max_area