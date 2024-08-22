from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highway = []
        for i in range(len(position)):
            highway.append([position[i], speed[i]])
        highway.sort(key=lambda x:x[0])
        time = []
        i = 0
        while i < len(highway):
            if highway[i][1] == 0:
                highway = highway[i+1:]
                time = []
                i = 0
            else:
                time.append((target - highway[i][0])/highway[i][1])
                i += 1
        #print(time)
        for i in range(len(time)-2,-1,-1):
            if time[i] <= time[i+1]:
                time.pop(i)
        return len(time)
        
"""
ACCEPTED ANSWER:
O(nlogn) time (I sorted it)
My thought process here was:
- Lets say cars did not have to wait for other cars
- Then each car would reach the target in terms of (target - position) / speed
- But cars have to wait for other cars
- So cars who have faster speeds than cars who are ahead of them will have the same time as the ones ahead
- But how do we figure out which cars are ahead of them?
    - I sorted the list for that, but there could be better solutions
- Then I compared with the car ahead. If the car reaches in less time than the car ahead, remove the car
- Then in the end, the length of the list will be all the cars
MOST COMMON SOLUTION:
- Basically the same as my answer
- They instead calculated time first and then sorted with position
- Then instead of popping the item, they just incremented a count based on how many times the time was greater than the max so far
- They also didnt handle the 0 speed case which I did. It said it was possible in the constraints but I guess it was not.
Below is what I tried initially
"""


class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        highway = []
        zero_value = -1
        for i in range(len(position)):
            if speed[i] == 0:
                zero_value = position[i]
                break
            elif zero_value >= 0 and zero_value >= position[i]:
                break
            highway.append([position[i], speed[i]])
        highway.sort(key=lambda x:x[0])
        count = 0
        size = len(highway)
        while highway:
            highway[-1][0] += highway[-1][1]
            print(len(highway)-1, highway[-1][0], size)
            i = len(highway) - 2
            while i >= 0:
                highway[i][0] += highway[i][1]
                print(i, highway[i][0], size)
                if(highway[i][0] > highway[i+1][0] or (highway[i][0] == highway[i+1][0] and highway[i][0] <= target) ):
                    print("remove:", i, highway[i][0], size)
                    highway.pop(i)
                size = len(highway)
                i -= 1
            j = len(highway)-1
            while highway and highway[j][0] >= target:
                print("reached:", j, highway[j][0], size)
                count += 1
                highway.pop(-1)
                j -= 1
                if highway:
                    print("next:", highway[j][0])
        return count

"""
ATTEMPTED ANSWER:
- This answer tries to incrementally add each speed to the positions, and then remove them if they reach the car ahead
- The issue with this is in the edge cases
    - A car can reaches another car every step
    - But if it reaches the car on the step where they both cross the target, I have to figure out if they reach before the target or after
    - This complicates the logic a lot (it is already pretty complicated), so I just changed approaches
"""