from collections import defaultdict

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphabet = defaultdict(int)
        for l in list('abcdeffghijklmnopqrstuvwxyz1234567890'):
            alphabet[l] = 1
        
        my_s = [l for l in s.lower() if alphabet[l]]

        return my_s==my_s[::-1]