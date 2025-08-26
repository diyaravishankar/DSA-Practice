class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = [False] * (n + 2)
        self.curr = 0
    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.curr + 1]:
            self.curr += 1
    def longest(self) -> int:
        return self.curr