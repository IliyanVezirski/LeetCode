class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        last_word = word_list[-1]
        counter = 0
        for letter in last_word:
            if letter.isalpha():
                counter += 1
        return counter