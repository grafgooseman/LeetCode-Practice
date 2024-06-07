class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = 0

        scores = [0, 0]

        for n in operations:
            try:
                scores.append(int(n))
                s = s + scores[-1]
            except:
                if n == "+":
                    scores.append(scores[-2] + scores[-1])
                    s = s + scores[-1]
                elif n == "D":
                    scores.append(scores[-1] * 2)
                    s = s + scores[-1]
                else: 
                    s = s - scores[-1]
                    scores.pop(-1)


        return s