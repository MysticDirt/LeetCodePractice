from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [0] * (len(nums) - k + 1)
        de = deque([nums[0]])
        for i in range(1, k):
            while de and de[-1] < nums[i]:
                de.pop()
            de.append(nums[i])
        result[0] = de[0]
        if de[0] == nums[0]:
            de.popleft()
        j = 0
        for i in range(k, len(nums)):
            while de and de[-1] < nums[i]:
                de.pop()
            de.append(nums[i])
            j += 1
            result[j] = de[0]
            if de[0] == nums[j]:
                de.popleft()
        
        return result

"""
6. Sliding Window Maximum
- O(n) time, iterates through array only once, and at maximum pushes and pops every element from the deque once
- This one I had to look at the NeetCode drawing solution, and then did the code myself
- At first I originally thought of using a heap, because all we'd have to do is maintain a maxheap of the values in the window and then it would be O(nlogn)
- But since its a LeetCode hard, it probably has an O(n) solution that is not as straightforward
- The things I did find myself:
    - I noticed that we did not have to care about the values before the current maximum in the window
    - I was thinking of using a stack/queue/deque which was on the right track
- The things I missed:
    - The main problem I was having was dealing with a test case where the current maximum value leaves the window without the next incoming value being the new max
        - For example, lets say our array is [9 7 8 6 5] with k = 3
        - We see [9 7 8] first, with a max of 9
        - Then we move on to [7 8 6]
        - Here the new max would be 8, but with a deque we only saw the 9 leave and the 6 come in
        - I was trying to figure out how would we know to get the 8 if we cannot currently see it
        - So I was thinking maybe we find the first and second maxes, and if the first max leaves we go to the second max
        - Then the problem remains of keeping the second max. If the second max leaves, we did not keep track of the third max to replace it
        - Then that made me think we need every value visible, so I thought heap was the only solution
        - Then I looked up the target time complexity and it was O(n), so back to the drawing board
        - So then I realized that we did not need to care about the things before the current max
        - But in the [9 7 8 6 5] -> [7 8 6], we don't know 8 is the new max until we scan 7 8 6, and then delete 7
    - In this whole process, what I missed is that not only do we not have to care about the things before the current max, we do not have to care about any number smaller than its successors that fits in the window
        - So in this case, when I scan [9 7 8], the moment I see 8 > 7, I just pop 7 out of the deque at first anyway
        - Then when I move on to the second window, I just see 8 > 6 and choose 8
        - Then the deque itself is always in a non-increasing order (decreasing with duplicates) 
        - This type of deque is called a Monotonic Deque
- So in the end, the algorithm is
    - Make a deque and a result array
    - Add the first window into the deque, removing any numbers smaller than their successors
        - To remove numbers smaller than their successors
            - First check if the deque's furthest number is smaller than your next number
            - If it is, pop it and check again. Keep popping until the deque's furthest number is bigger or equal to your next number
            - Then add your number to the deque
    - Then, the first number in the deque is your maximum
    - If the first number in the deque matches the number in the beginning of the window, then pop it off the deque to move the window forward
    - Then loop through the rest of the array, adding the next number to the deque (same removal process), take the first number as the max, and remove the first number if it is the same as the beginning of the current sliding window
    - Then return the result
"""