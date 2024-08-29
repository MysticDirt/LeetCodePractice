from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        if not nums1:
            #print("skip1")
            middle2 = (len(nums2) // 2)
            if len(nums2) % 2 == 0:
                return (nums2[middle2] + nums2[middle2-1]) / 2
            else:
                return nums2[middle2]
        a = len(nums1)
        b = len(nums2)
        n = a + b
        partition_target = n // 2
        even = (n % 2) == 0
        left = -1
        right = a
        middle = a//2
        middle2 = b//2
        while left <= right:
            middle = left + (right - left) // 2
            middle2 = partition_target - middle - 1
            #print(middle, middle2)
            if middle < 0 or middle2 >= b or nums1[middle] <= nums2[middle2]:
                if middle2 - 1 < 0 or middle + 1 >= a or nums1[middle + 1] >= nums2[middle2 - 1]:
                    break
                else:
                    left = middle + 1
            else:
                right = middle - 1
            #print(middle, middle2, ":", left, right)
        #print(middle, middle2)
        def maxcheck(num1, num2):
            if num1 >= a or num1 < 0:
                return nums2[num2]
            elif num2 >= b or num2 < 0:
                return nums1[num1]
            else:
                return max(nums1[num1], nums2[num2])
        def mincheck(num1, num2):
            if num1 >= a or num1 < 0:
                return nums2[num2]
            elif num2 >= b or num2 < 0:
                return nums1[num1]
            else:
                return min(nums1[num1], nums2[num2])
        if even:
            return (maxcheck(middle, middle2 - 1) + mincheck(middle + 1, middle2)) / 2
        else:
            #print("normal")
            return mincheck(middle + 1, middle2)
        

"""
CORRECT SOLUTION:
Initial attempt below this long explanation
I watched the NeetCode video for the explanation of the logic but not the code, and then tried implementing the code myself.
It took me a while, around 2 hours, to sort out the bugs in the code.
O(log(m+n)) where m is the length of nums1 and n is the length of nums2
In my initial attempt I was thinking of trying to converge on the median using binary search, but I took the more common approach here
Thinking in terms of partitions:
    - The median is in the center of array, which means it has equal length partitions on the left and right of it.
    - On odd length partition arrays, the partition does not include the center number, the median.
    - Ex: [1 2 3 4 5 6] 7 [8 9 10 11 12 13]
        - Each partition has 6 numbers in an array of length 13. 
    - The partition length is the length of the total array divided by 2 floored.
    - so (a + b) // 2
    - This makes it so that we do not have to search the other array, only one array.
        - Ex: [1 3 5 5 7], [1 3 4 9]
            - Lets say we search [1 3 4 9] and start with 4 as our middle (4 // 2 = 2)
            - Lets designate our middle as the last number of the left partition on this array.
            - So [1 3 4] are all in the left partition, while [9] is not.
            - Since we already know the target partition is (a + b)//2, 9//2 = 4 is our target partition.
            - So on the right array, we just put it so that [1] on the left partition while the rest are on the right or center
                - Because our left partition [1 3 4] has length 3 and we only need one more number to reach our target length of 4
                - Other lengths are not possible for this combination of arrays, so we will only check this one
            - So our partitions are:
                - [(1) 3 5  5 7]
                - [(1  3 4) 9]
            - If we chose the correct left partition, then all the numbers on the right should be greater than or equal to our max
                left partition
            - But we did not. The 3 on the first array is greater than the 4 on the second array.
                - We only have to compare the max (rightmost) left partition and the min (leftmost) right partition / center member
                    of alternate arrays because the arrays are sorted.
                - So within the same array it is guaranteed that the left is greater than or equal to the right
            - That means that 4, our initial middle, is too big. We need to search smaller.
            - So we search the bottom half of the array, [1 3]. 
            - We choose 3 as our middle, our maximum left partition value on this array, and 4 - 2 = 2, so our partitions become
                - [(1 3) 5 5 7]
                - [(1 3) 4 9]
            - 3 <= 5 and 3 <= 4, so we got the correct partition. Now, which one is the median?
            - Since the total length of the two arrays is odd, the median is just one number
            - And that number is the number that is in neither the left or right partition, but is in the center.
            - But we do not keep track of the right partition, and since the array is sorted the next least greatest number from the 
                left partition is the median.
            - So we compare the two numbers from both arrays after the left partition and choose the minimum.  
            - In the example, we compare 5 and 4 and choose 4. Thus, 4 is our median.
        - In an even lenght example, we instead choose the maximum from the two right numbers on the left partition plus the mininum
            from the two left numbers on the right partition divided by 2.
    - We always search the array with the least length to minimize time taken.
    - There are edge cases where the left or right partition takes up the entire array or none of the array.
    - In my solution I use -1 and the length of the array to indicate that.
    - If the index ends up being outside of the array, I ignore it when finding the max or min of the numbers.
This is the 3rd LeetCode hard problem I attempted and the first hard problem where I had to seek outside help.
I do think my initial approach could have worked if I spent the time to debug it, but this is a little more straightforward and only
requires to search one array.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #print("test")
        left1 = 0
        left2 = 0
        right1 = len(nums1) - 1
        right2 = len(nums2) - 1
        if not nums1:
            #print("skip1")
            middle2 = left2 + ((right2 - left2) // 2)
            if len(nums2) % 2 == 0:
                return (nums2[middle2] + nums2[middle2+1]) / 2
            else:
                return nums2[middle2]
        elif not nums2:
            #print("skip2")
            middle1 = left1 + ((right1 - left1) // 2)
            if len(nums1) % 2 == 0:
                return (nums1[middle1] + nums1[middle1+1]) / 2
            else:
                return nums1[middle1]
        while left1 < right1 or left2 < right2:
            middle1 = (left1 + right1) // 2
            middle2 = (left2 + right2) // 2
            #if nums1[middle1] == nums2[middle2]:
                #left1 = right1 = middle1
                #left2 = right2 = middle2
                #break
            if nums1[middle1] > nums2[middle2]:
                right1 = middle1
                left2 = middle2 + 1
            else:
                left1 = middle1 + 1
                right2 = middle2
        #print(left1, right1)
        #print(left2, right2)
        #print(nums1, nums2)
        if (len(nums1) + len(nums2)) % 2 == 1:
            if nums1[left1] < nums2[left2]:
                return nums1[left1]
            else:
                return nums2[left2]
        else:
            if nums1[left1] < nums2[left2]:
                if left1 == len(nums1) - 1:
                    return (nums1[left1] + nums2[left2]) / 2
                else:
                    return (nums1[left1] + min(nums2[left2], nums1[left1+1])) / 2
            elif nums1[left1] > nums2[left2]:
                if left2 == len(nums2) - 1:
                    return (nums2[left2] + nums1[left1]) / 2
                else:
                    return (nums2[left2] + min(nums1[left1], nums2[left2+1])) / 2
            else:
                #if nums1[left] - 1 == len(nums1):
                  #  if nums
                return nums1[left1]
        #return 4.0
"""
INCORRECT SOLUTION
This is my attempt at the problem:
First I check if any list is empty, then I just return the median of that single list
Then I do the actual algorithm
Here is what I came up with:
    - Lets say the length of the first list is a, and the length of the second list is b.
    - The median will be at position (a + b) / 2 for the full list if merged
    - But we cannot merge it because that is an O(n) operation. We need this in O(log(a+b))
    - So I start by finding the medians of the two arrays
    - If one median is bigger than the other, then the real median must be between the two mini medians
        - One list is the "lower" list with the lower median, and the other is the higher list
        - So in the total combined list, the real median has to be somewhere in between the low and high
    - So we compare the medians. If list 1's median is bigger than list 2, then we know
        - The real median is less than list 1's median but bigger than list 2's median
        - So the right half of list 1 is eliminated and the left half of list 2 is eliminated.
        - Then we repeat with the remain lists
    - Then it eventually converges on one value while left < right for both arrays
    - If it is an odd number, take the min and use it
    - If it is an even number length list total, then use the converged number and the min of the next or other array number
However there are certain problems:
     - Handling each case at the end is a hassle. There must be a cleaner way
     - Sometimes it converges on the wrong number.
        - [1,3,7,8,9] and [3,7,8,9,11,14,16,18,20,21] converge on the first list 8 and second list 9
        - Here, 9 is the right answer, but since we take the minimum always it took 8
     - So I am pretty sure I got the general binary search idea right but somewhere in the implementation I took a wrong turn.
"""
