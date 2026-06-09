class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        car = [(0,1), (1,2), (4,2), (7,1)]

        1. Join positions and speeds
        cars = [(1,3),(4,2)]
        2. Sort the new array
        cars = [(1,3),(4,2)]
        3. Create a stack to contain the fleets
        stack = []
        4. Iterate the cars array from right to left
        5. Add two cars to the stack
        6. Check if the two cars arriving time intercepts
        7. Pop the last car if they intercept
        8. Return the lenght of the stack
        '''
        cars = []
        for i in range(len(position)):
            car_tuple = (position[i],speed[i])
            cars.append(car_tuple)

        cars = sorted(cars)
        stack = [cars[-1]]

        i = -2
        for car in reversed(cars[:-1]):
            stack.append(car)
            c1p, c1s = stack[-2]
            c2p, c2s = stack[-1]

            c1t = (target - c1p)/c1s
            c2t = (target - c2p)/c2s

            if c2t <= c1t:
                stack.pop()

        return len(stack)

        