class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            fn_id, typ, t = log.split(":")
            fn_id, t = int(fn_id), int(t)
            if typ == "start":
                if stack:
                    res[stack[-1]] += t - prev_time
                stack.append(fn_id)
                prev_time = t
            else:
                res[stack.pop()] += t - prev_time + 1
                prev_time = t + 1
        return res