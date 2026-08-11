class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:

            while stack and a < 0 and stack[-1] > 0:
                collision = a + stack[-1]

                if collision > 0:
                    a = 0
                elif collision < 0:
                    stack.pop()
                else:
                    stack.pop()
                    a = 0
            if a:
                stack.append(a)

        return stack
                    