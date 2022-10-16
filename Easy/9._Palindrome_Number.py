class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_backward_result = []
        x_forward_result = []
        for n in x_str:
            x_forward_result.append(n)
            x_backward_result.append(n)
        x_backward_result.reverse()
        if x_backward_result == x_forward_result:
            return True
        else:
            return False