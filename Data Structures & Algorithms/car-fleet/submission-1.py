class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # sort by position desc
        fleets = 0
        max_time = -1.0
        for pos, spd in cars:
            t = (target - pos) / spd
            if t > max_time:
                fleets += 1
                max_time = t
            # else: merges into the fleet ahead
        return fleets