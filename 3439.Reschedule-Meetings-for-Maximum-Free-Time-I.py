from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        gaps.append(startTime[0] - 0)
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        window = sum(gaps[:k+1])
        res = window
        idx = 0

        for i in range(k+1, len(gaps)):
            window = window - gaps[idx] + gaps[i]
            res = max(res, window)
            idx += 1
        return res
