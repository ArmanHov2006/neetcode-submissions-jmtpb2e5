class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                prev = st.pop()
                final[prev] = i - prev

            st.append(i)

        return final