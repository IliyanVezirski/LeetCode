class Solution:
    def plusOne(self, digits: list):
        string_numbers = [str(i) for i in digits]
        string_numbers = ''.join(string_numbers)
        int_numbers = int(string_numbers)
        new_number = int_numbers + 1
        new_number = str(new_number)
        new_number = [i for i in new_number]
        return new_number
