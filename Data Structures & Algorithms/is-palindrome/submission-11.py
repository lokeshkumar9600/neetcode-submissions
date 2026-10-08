class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while(left < right):
            if not s[right].isalnum() and left <= right:
                right -= 1
                continue

            
            if not s[left].isalnum() and left <= right:
                left += 1
                continue

            if(s[left].lower() != s[right].lower()):
                return False
            else:
                left += 1
                right -= 1
            
        
        
        return True
        