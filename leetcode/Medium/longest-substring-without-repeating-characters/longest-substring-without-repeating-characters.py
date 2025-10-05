class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # to store characters in current window
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If character is already in window, shrink from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add new character
            char_set.add(s[right])
            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
