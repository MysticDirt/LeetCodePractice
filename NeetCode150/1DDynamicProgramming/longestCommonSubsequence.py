class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        letter_count = [[0] * len(text2) for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i > 0 and j > 0:
                        letter_count[i][j] = 1 + letter_count[max(i-1,0)][max(j-1, 0)]
                    else:
                        letter_count[i][j] = 1
                else:
                    # print(i)
                    letter_count[i][j] = max(letter_count[max(i-1,0)][j], letter_count[i][max(j-1, 0)])
        # print(letter_count)
        return letter_count[i][j]
    
"""
Not NeetCode150 but, still a classic
Above is my solution. I build a 2D array that essentially counts the length of the longest common subsequence of the first i letters in text1 and the first j letters of text 2.
Then the length only increases if the last letter of both substrings match. Otherwise it stays the same.
Ways to make it faster:
Only need a 1D array since only the current and previous row matters.
Or add a buffer row and column of all zeros so I don't have to do the max checks to prevent out of bounds accesses, but this is still 2D.
"""