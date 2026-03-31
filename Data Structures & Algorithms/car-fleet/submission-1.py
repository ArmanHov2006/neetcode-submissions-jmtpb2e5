class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        cars = sorted(zip(position, speed), reverse=True)
        for p, s in cars:
            arr_time = (target - p) / s
            arr.append(arr_time)
        st = []
        for time in arr:
            if not st or time > st[-1]:
                st.append(time)
        return len(st)